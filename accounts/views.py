from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from .forms import (
    LoginForm,
    SignUpForm,
    ForgotPasswordForm,
    ResetPasswordForm
)
from django.views.generic import View
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group
from django.forms import ValidationError
from django.contrib.auth import get_user_model

from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.debug import sensitive_post_parameters
import datetime
from .forms import PasswordRecoveryForm, PasswordResetForm
from .signals import user_recovers_password


User = get_user_model()

class LoginView(View):
    def get(self,request):
        form = LoginForm(request.POST or None)
        return render(request, "accounts/login.html", {"form": form })

    def post(self,request):
        form = LoginForm(request.POST or None)

        msg = None

        if request.method == "POST":

            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    if not user.is_superuser and not user.is_staff:
                        user.is_staff = True
                        user.save()
                    if not (user.is_superuser or user.groups.filter(name='admin').exists()) and user.groups.filter(name='client').exists():
                        # user.groups.add(Group.objects.get(name='client'))
                        user.save()
                    return redirect("core/dashboard/")
                else:
                    # messages.add_message(request, messages.WARNING, 'User name and password does not match')
                    msg = ('User name/Email and password does not match',)
                    form.fields['email'].widget.attrs['class']="form-control is-invalid"
                    form.fields['password'].widget.attrs['class']="form-control is-invalid"
                    form.add_error("email",ValidationError(msg[0]))
            else:
                msg = ('Please fill all the required fields',)
                form.add_error("email",ValidationError(msg[0]))
                print("field requires")

        return render(request, "accounts/login.html", {"form": form, "msg" : msg})

class ForgotPasswordView(View):
    def get(self,request):
        form = ForgotPasswordForm(request.POST or None)
        return render(request, "accounts/forgot-password.html", {"form": form })

    def post(self,request):
        form = ForgotPasswordForm(request.POST or None)

        msg = None

        if request.method == "POST":

            if form.is_valid():
                email = form.cleaned_data.get("email")
                is_user = User.objects.filter(email=email).exists()
                if is_user:
                    reset_form = ResetPasswordForm(initial={"email":email})
                    return render(request, "accounts/reset-password.html", {"form": reset_form, "msg" : msg})
                else:
                    # messages.add_message(request, messages.WARNING, 'User name and password does not match')
                    print(email)
                    msg = ('Enter the email address registered on your account',)
                    form.fields['email'].widget.attrs['class']="form-control is-invalid"
                    form.add_error("email",ValidationError(msg[0]))
            else:
                msg = ('Please fill all the required fields',)
                form.add_error("email",ValidationError(msg[0]))
                print("field requires")

        return render(request, "accounts/forgot-password.html", {"form": form, "msg" : msg})

class ResetPasswordView(View):
    def get(self,request):
        form = ResetPasswordForm(request.POST or None)
        return render(request, "accounts/forgot-password.html", {"form": form })

    def post(self,request):
        form = ResetPasswordForm(request.POST or None)

        if request.method == "POST":

            if form.is_valid():
                email = form.cleaned_data.get("email")
                password1 = form.cleaned_data.get("password1")
                
                user = User.objects.get(email=email)
                user.set_password(password1)
                user.save()
                return redirect("accounts:login")

        return render(request, "accounts/reset-password.html", {"form": form })

class RegisterView(View):
    def get(self,request):
        form = SignUpForm(request.POST or None)
        return render(request, "accounts/register.html", {"form": form })

    def post(self, request):
        msg     = None
        success = False

        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # group = Group.objects.get(name='client')
                username = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)
                # user.groups.add(group)

                msg     = messages.add_message(request, messages.SUCCESS,'User created Successfully, Please Login!')
                success = True
                
                return redirect("/core/dashboard/")

            else:
                msg = ('Form is not valid',)
                form.add_error(None,'Form is not valid')
        else:
            form = SignUpForm()

        return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class SaltMixin(object):
    salt = 'password_recovery'
    url_salt = 'password_recovery_url'


def loads_with_timestamp(value, salt):
    """Returns the unsigned value along with its timestamp, the time when it
    got dumped."""
    try:
        signing.loads(value, salt=salt, max_age=-999999)
    except signing.SignatureExpired as e:
        age = float(str(e).split('Signature age ')[1].split(' >')[0])
        timestamp = timezone.now() - datetime.timedelta(seconds=age)
        return timestamp, signing.loads(value, salt=salt)


class RecoverDone(SaltMixin, generic.TemplateView):
    template_name = 'accounts/reset_sent.html'

    def get_context_data(self, **kwargs):
        ctx = super(RecoverDone, self).get_context_data(**kwargs)
        try:
            ctx['timestamp'], ctx['email'] = loads_with_timestamp(
                self.kwargs['signature'], salt=self.url_salt,
            )
        except signing.BadSignature:
            raise Http404
        return ctx

class Recover(SaltMixin, generic.FormView):
    case_sensitive = True
    form_class = PasswordRecoveryForm
    template_name = 'accounts/recovery_form.html'
    success_url_name = 'accounts:password_reset_sent'
    email_template_name = 'accounts/recovery_email.txt'
    email_subject_template_name = 'accounts/recovery_email_subject.txt'
    search_fields = ['username', 'email']

    def get_success_url(self):
        return reverse(self.success_url_name, args=[self.mail_signature])

    def get_context_data(self, **kwargs):
        kwargs['url'] = self.request.get_full_path()
        return super(Recover, self).get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(Recover, self).get_form_kwargs()
        kwargs.update({
            'case_sensitive': self.case_sensitive,
            'search_fields': self.search_fields,
        })
        return kwargs

    def get_site(self):
        return get_current_site(self.request)

    def send_notification(self):
        context = {
            'site': self.get_site(),
            'user': self.user,
            'username': self.user.get_username(),
            'token': signing.dumps(self.user.pk, salt=self.salt),
            'secure': self.request.is_secure(),
        }
        body = loader.render_to_string(self.email_template_name,
                                       context).strip()
        subject = loader.render_to_string(self.email_subject_template_name,
                                          context).strip()
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                  [self.user.email])

    def form_valid(self, form):
        self.user = form.cleaned_data['user']
        self.send_notification()
        if (
            len(self.search_fields) == 1 and
            self.search_fields[0] == 'username'
        ):
            # if we only search by username, don't disclose the user email
            # since it may now be public information.
            email = self.user.username
        else:
            email = self.user.email
        self.mail_signature = signing.dumps(email, salt=self.url_salt)
        return super(Recover, self).form_valid(form)

class Reset(SaltMixin, generic.FormView):
    form_class = PasswordResetForm
    token_expires = None
    template_name = 'accounts/reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')

    def get_token_expires(self):
        duration = getattr(settings, 'PASSWORD_RESET_TOKEN_EXPIRES',
                           self.token_expires)
        if duration is None:
            duration = 3600 * 48  # Two days
        return duration

    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.user = None

        try:
            print(kwargs['token'])
            print(self.get_token_expires())
            pk = signing.loads(kwargs['token'],
                               max_age=self.get_token_expires(),
                               salt=self.salt)
            print("pk =",pk)
        except signing.BadSignature:
            print("invalide")
            return self.invalid()

        self.user = get_object_or_404(get_user_model(), pk=pk)
        return super(Reset, self).dispatch(request, *args, **kwargs)

    def invalid(self):
        return self.render_to_response(self.get_context_data(invalid=True))

    def get_form_kwargs(self):
        kwargs = super(Reset, self).get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(Reset, self).get_context_data(**kwargs)
        if 'invalid' not in ctx:
            ctx.update({
                'username': self.user.get_username(),
                'token': self.kwargs['token'],
            })
        return ctx

    def form_valid(self, form):
        form.save()
        user_recovers_password.send(
            sender=get_user_model(),
            user=form.user,
            request=self.request
        )
        return redirect(self.get_success_url())

class ResetDone(generic.TemplateView):
    template_name = 'accounts/recovery_done.html'

