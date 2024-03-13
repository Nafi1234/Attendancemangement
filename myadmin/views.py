from django.shortcuts import render,redirect
from django.contrib import auth
from .models import CustomUser,Semesterss,FacultyDetails
from django.http import Http404
from django.http import HttpResponse
from faculty.models import StudentDetails

def admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None and user.is_superuser:
            pass
        
def register_students(request):

    if request.method == 'POST':
    
        email = request.POST.get('email')
        name = request.POST.get('name')
        user_type = 'S' 
        password = request.POST.get('password')
        semester=request.POST.get('semester') 
        newuser=CustomUser.objects.create_user(email=email, name=name, user_type=user_type, password=password)
        StudentDetails.objects.create(student_name=newuser,student_semester=semester)
        
    
        return redirect('studentlogin') 

    return render(request, 'studentregister.html')
def studentlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(request,email=email,password=password)
        if user is not None and user.user_type is 'S':
            redirect()
# def register_faculty(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_type = request.POST.get('user_type')


#         faculty_user = CustomUser.objects.create_user(email=email, name=name, user_type=user_type, password=password)


#         semesters = request.POST.getlist('semesters[]')
#         subjects = request.POST.getlist('subjects[]')
#         for semester_name, subject_name in zip(semesters, subjects):
#             semester = Semesterss.objects.create(semester_no=semester_name, subject=subject_name)
#             FacultyDetails.objects.create(name=faculty_user, semester_taught=semester)

#         return HttpResponse("Faculty registered successfully.")
#     else:
#         return render(request, 'facultyregister.html')
