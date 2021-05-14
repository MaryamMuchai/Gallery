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
    def