# Generated by Django 3.2.12 on 2023-03-03 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_destinations_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinations',
            old_name='status',
            new_name='is_add',
        ),
    ]
