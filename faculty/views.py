from django.shortcuts import render,redirect
from myadmin.models import CustomUser
from .models import TeacherDetails,Year,AttendanceMarkings
from django.http import HttpResponse
def register_faculty(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')


        faculty_user = CustomUser.objects.create_user(email=email, name=name, user_type=user_type, password=password)


        semesters = request.POST.getlist('semesters[]')
        subjects = request.POST.getlist('subjects[]')
        for semester_name, subject_name in zip(semesters, subjects):
            semester = Year.objects.create(semesters_no=semester_name, subject=subject_name)
            TeacherDetails.objects.create(faculty=faculty_user, semester_taught=semester)

        return redirect('faculty_login')
    else:
        return render(request, 'facultyregister.html')
