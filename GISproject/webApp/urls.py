from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



app_name = 'webApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('search_results/', views.search_results, name='search_results'),
    path('map/', views.emassyMap, name='map'),
    path('about/', views.about, name='about'),
]

