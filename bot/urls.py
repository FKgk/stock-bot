from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.set_urls, name='set_urls'),
]
