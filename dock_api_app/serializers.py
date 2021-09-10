from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', '', 'vehicleTitle', 'make', 'model', 'year', 'engine', 'bodyStyle', 'driveTrain')
        model = Vehicle