# Generated by Django 3.2.12 on 2023-03-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20230316_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectdestinations',
            name='destination_id',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
