"""trading_bot URL Configuration
"""

from django.urls import path
from .views import (
    LoginView,
    RegisterView,
    LogoutView,
    ForgotPasswordView,
    ResetPasswordView,

    Recover,
    RecoverDone,
    Reset,
    ResetDone,
)

# from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #import this

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('forgot-password/', ForgotPasswordView.as_view(), name="forgot-password"),
    # path('reset-password/', ResetPasswordView.as_view(), name="reset-password"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path(r'recover/(<signature>)/', RecoverDone.as_view(), name='password_reset_sent'),
    path('recover/', Recover.as_view(), name='password_reset_recover'),
    path('reset/done/', ResetDone.as_view(), name='password_reset_done'),
    path(r'reset/(<token>)/', Reset.as_view(), name='password_reset_reset'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
