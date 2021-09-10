from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

# Create your models here.
def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Vehicle(models.Model):
    driverName = models.ForeignKey
    vehicleTitle = models.CharField(max_length=40)
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.PositiveIntegerField(default= current_year(), validators=[MinValueValidator(1930), max_value_current_year])
    engine = models.CharField(max_length=60)
    bodyStyle = models.CharField(max_length=60)
    driveTrain = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.make