# Generated by Django 3.2.7 on 2021-09-09 03:45

import django.core.validators
from django.db import migrations, models
import dock_api_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleTitle', models.TextField(max_length=40)),
                ('make', models.CharField(max_length=60)),
                ('model', models.CharField(max_length=60)),
                ('year', models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1930), dock_api_app.models.max_value_current_year])),
                ('engine', models.CharField(max_length=60)),
                ('bodyStyle', models.CharField(max_length=60)),
                ('driveTrain', models.CharField(max_length=60)),
            ],
        ),
    ]
