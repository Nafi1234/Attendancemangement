from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
path('facultyregister',views.register_faculty,name="register_faculty"),
]
 