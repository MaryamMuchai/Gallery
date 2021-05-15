from django.test import TestCase
from .models import Category, Image, Location
# Create your tests here.
class CategoryTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.category = Category(title='animals')
        self.category.save_category()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name="kenya")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Mombasa')
        self.location.save_location()
        
        self.category = Category(title ='place')
        self.category.save_category()
        self.image_test = Image(id=1, name='image', description="testing", location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        before = Image.objects.all()
        self.assertTrue(len(before) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_by_id(self):
        f_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(f_image, image) 
