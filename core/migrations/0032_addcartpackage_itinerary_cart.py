# Generated by Django 3.2.12 on 2023-01-04 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20230104_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcartpackage',
            name='itinerary_cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.itinerary'),
        ),
    ]
