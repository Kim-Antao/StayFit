from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('cache_subscribe_data/', views.cache_subscribe_data, name='cache_subscribe_data'),
]
