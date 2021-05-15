from django.shortcuts import render, redirect
from .models import Location, Image, Category
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def index(request):
    image = Image.objects.all()
    locations = Location.get_locations()
    category = Category.objects.all() 
    print(locations)
    return render(request, 'index.html', {'image': image[::-1], 'locations': locations, 'category':category})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch") 
        searched_image = Image.search_by_category(category)
        message = f"{category}"
        print(searched_image)
        return render(request, 'index.html',{"message":message,"all_images": searched_image})
    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})

def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__category_name = category)
    return render(request,'index.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})

def image_location(request,location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request,'index.html',{'location_images':images})


    
