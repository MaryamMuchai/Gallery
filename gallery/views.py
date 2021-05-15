from django.shortcuts import render, redirect
from .models import Location, Image, Category

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.locations()
    category = Category.objects.all() 
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations, 'category':category})
