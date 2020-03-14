from django.urls import path, include
import views

urlpatterns = [
    path('/', views.set_urls, name='set_urls')
]
