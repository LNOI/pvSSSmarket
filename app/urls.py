
from django.contrib import admin
from django.urls import path
from .views import Home,add, edit,delete,update
urlpatterns = [
    path('',Home ),
    path('add',add), 
    path('edit',edit),
    path('update/',update), 
    path('delete/',delete), 
]
