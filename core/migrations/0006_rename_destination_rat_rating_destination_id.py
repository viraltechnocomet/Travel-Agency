# Generated by Django 3.2.12 on 2023-02-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_user_rating_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='destination_rat',
            new_name='destination_id',
        ),
    ]