from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self) -> str:
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def delete_location(self):
        self.delete()

    def save_location(self):
        self.save()
        
