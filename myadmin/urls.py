
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [


    path('studentresgisteration',views.register_students,name="register_students")
]
