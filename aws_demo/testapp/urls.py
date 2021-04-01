from django.contrib import admin
from django.urls import path
from .views import index,type_my_name

urlpatterns = [
    path('', index),
    path('print_me/<str:name>',type_my_name)
]