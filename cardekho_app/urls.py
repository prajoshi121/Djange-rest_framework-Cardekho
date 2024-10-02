from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('car/', views.car_list_view, name='car_list'),
    path('car/<int:pk>/', views.car_detail_view, name='car_detail')
    
]