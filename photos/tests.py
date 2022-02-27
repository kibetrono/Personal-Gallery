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

    def test_save_method(self):
        """Testing Save Method"""
        self.place.save_location()
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)

    def test_update_method(self):
        """Testing Update Method"""
        self.place.update_location(name="Nakuru")
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.place.delete_location()
        places = Location.objects.all()
        self.assertTrue(len(places) < 1)

    def test_location_return_str(self):
        """Testing str Method"""
        loc = Location.objects.get(location_name="Nairobi")
        self.assertEqual(str(loc), "Nairobi")

    def tearDown(self):
        """tearDown method"""
        Location.objects.all().delete()

class CategoryTestClass(TestCase):

    def setUp(self):
        """Creating a new category and saving it"""
        self.category = Category(category_name='news')
        self.category.save_category()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        """Testing Update Method"""
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_update_method(self):
        """Testing Update Method"""
        self.category.update_category(name="fashion")
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) < 1)

    def test_category_return_str(self):
        """Testing return str Method"""
        cat = Category.objects.get(category_name="news")
        self.assertEqual(str(cat), "news")

    def tearDown(self):
        """tearDown method"""
        Category.objects.all().delete()