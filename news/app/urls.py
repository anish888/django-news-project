from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   #adding path of the index function
    path('',views.index),
]
