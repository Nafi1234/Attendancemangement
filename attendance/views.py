from django.shortcuts import render
from django.contrib import auth


def adminlogin(request):
    return render(request, "adminlogin.html")

def studentlogin(request):
    return render(request, "studentlogin.html")
def studentregister(request):
    return render(request,"studentregister.html")