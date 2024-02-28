from django.shortcuts import render,redirect
from django.contrib import auth
from .models import CustomUser


def admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None and user.is_superuser:
            pass
        
def register_students(request):
    print("true")
    if request.method == 'POST':
        print("helo",request)
        email = request.POST.get('email')
        name = request.POST.get('name')
        user_type = 'S' 
        password = request.POST.get('password')

    
    
        
        newuser=CustomUser.objects.create(email=email, name=name, user_type=user_type, password=password)
        print("sucees")
        return redirect('studentlogin') 

    return render(request, 'studentregister.html')