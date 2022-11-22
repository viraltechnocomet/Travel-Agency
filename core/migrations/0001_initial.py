# Generated by Django 3.2.12 on 2022-11-22 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=550, unique=True)),
                ('data_image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('budget', models.FloatField()),
                ('befor_you_go', models.TextField()),
                ('nature', models.CharField(max_length=250)),
                ('website', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('gps_cordinate', models.CharField(max_length=500)),
                ('spend_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.images')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=250, unique=True)),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.activity')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
                ('itinerary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.itinerary')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Selected_Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.IntegerField()),
                ('costing', models.FloatField(max_length=100)),
                ('arriaval_time', models.DateTimeField()),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.package')),
                ('use_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
