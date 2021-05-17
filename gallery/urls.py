from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "gallery"

urlpatterns = [
    path('',views.index,name='index'),
    path('search/', views.search_results, name='search_results'),
    #path('category/(\w+)', views.get_category,name='get_category'),
    path('location/<location>/',views.image_location, name = 'location') 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 