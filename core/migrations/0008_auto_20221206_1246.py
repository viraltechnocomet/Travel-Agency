# Generated by Django 3.2.12 on 2022-12-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_itinerary_activity_name_itinerary_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='data_image',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='image_id',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='data_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]