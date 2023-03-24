# Generated by Django 3.2.12 on 2023-03-16 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0038_auto_20230316_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinations',
            name='is_add',
        ),
        migrations.CreateModel(
            name='SelectDestinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('details', models.ManyToManyField(blank=True, to='core.Itinerary')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]