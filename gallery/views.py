from django.shortcuts import render, redirect
from .models import Location, Image, Category
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations})

def search_results(request):
    
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"all_images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__category_title = category)
    return render(request,'index.html',{'category_results':category_results,'location_results':location_results})

def image_location(request,location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'locs.html', {'location_images': images})
    
#def location(request, pk):
    #images = Image.objects.get(id=pk)
    #return render(request, 'locs.html', {'images':Image})