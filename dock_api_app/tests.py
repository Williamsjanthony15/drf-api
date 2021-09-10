from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Vehicle

class VehicleTest(TestCase):

    @classmethod
    def testData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_vehicle = Vehicle.objects.create(
            vehicleTitle = 'My Favorite Vehicle',
            make = 'Ford',
            model = 'F-150',
            year = '2018',
            engine = 'Coyote',
            bodyStyle = 'Super Crew Cab',
            driveTrain = '4x4'
        )
        test_vehicle.save()

    def test_vehicle_save(self):
        vehicle = Vehicle.objects.get(id=1)
        actual_vehicleTitle = str(Vehicle.vehicleTitle)
        actual_make = str(Vehicle.make)
        actual_model = str(Vehicle.model)
        actual_year = int(Vehicle.year)
        actual_engine = str(Vehicle.engine)
        actual_bodyStyle = str(Vehicle.bodyStyle)
        actual_driveTrain = str(Vehicle.driveTrain)
        self.assertEqual(actual_vehicleTitle, 'My Favorite Vehicle')
        self.assertEqual(actual_make, 'Ford')
        self.assertEqual(actual_model, 'F-150')
        self.assertEqual(actual_year, '2018')
        self.assertEqual(actual_engine, 'Coyote')
        self.assertEqual(actual_bodyStyle, 'Super Crew Cab')
        self.assertEqual(actual_driveTrain, '4x4')


# Create your tests here.
