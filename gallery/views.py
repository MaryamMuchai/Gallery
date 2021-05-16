from django.shortcuts import render, redirect
from .models import Location, Image, Category
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    category_results = Category.objects.all() 
    print(locations)
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations, 'category_results':category_results})

def search_results(request):
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem") 
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'index.html',{"message":message,"all_images": searched_image})
    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})

def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__category_title = category)
    return render(request,'index.html',{'category_results':category_results,'location_results':location_results})

def image_location(request,location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'index.html', {'location_images': images})
    
