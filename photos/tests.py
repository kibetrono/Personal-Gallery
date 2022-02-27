from django.test import TestCase
from .models import Image, Location, Category


# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        """Creating a new location and saving it"""
        self.place = Location(location_name='Nairobi')
        self.place.save_location()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.place, Location))
