# Generated by Django 3.2.7 on 2021-09-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dock_api_app', '0002_alter_vehicle_vehicletitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicleTitle',
            field=models.TextField(max_length=40),
        ),
    ]
