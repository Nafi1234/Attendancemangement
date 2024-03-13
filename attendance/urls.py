"""
URL configuration for attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('',views.studentlogin,name="studentlogin"),
    path('studentresgister',views.studentregister,name="register_student"),
    path('facultylogin',views.facultylogin,name="faculty_login"),
    path('facultydetail<int:user_id>/', views.user_detail_view, name='faculty_detail'),
    path('studentdetail<int:user_id>/',views.studentdetailview,name="studentdetail"),
    path('facultydetail<int:user_id>/add_attendance/', views.studentattendance, name='add_attendance'),
    path('studentattendance<int:user_id>/',views.viewstudentattendance,name="student_attendance"),
    path('submited_attendance/',views.submit_attendance,name="submited_attendance"),

    path('register',include('myadmin.urls')),
    path('faculty/',include('faculty.urls'))
]
