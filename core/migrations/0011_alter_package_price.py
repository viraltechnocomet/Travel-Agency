# Generated by Django 3.2.12 on 2022-12-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20221213_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.CharField(max_length=250, null=True),
        ),
    ]