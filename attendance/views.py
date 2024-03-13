from django.shortcuts import render,redirect
from django.contrib import auth
from myadmin.models import CustomUser
from faculty.models import TeacherDetails,StudentDetails
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from faculty.models import AttendanceMarkings
from django.utils import timezone
from django.urls import reverse


def adminlogin(request):
    return render(request, "adminlogin.html")

from django.contrib.auth.models import User

def studentlogin(request):

    if request.method == "POST":
        print("ffasd")
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        
        user = auth.authenticate(email=email,password=password)
        print(user)
        if user is not None and user.is_authenticated and user.user_type == 'S':
            return redirect('studentdetail', user_id=user.id)
        else:
            error_message = "Invalid email or password"
            return render(request, "studentlogin.html", {'error_message': error_message})
    else:
        return render(request, "studentlogin.html")

def studentregister(request):
    return render(request,"studentregister.html")
def facultylogin(request):
    if request.method == 'POST':
        email=request.POST['email']
        
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        
        if user is not None:
            print(user)
            return redirect('faculty_detail', user_id=user.id)
    
        else:
            return render(request,"facultylogin.html")
    else:
        return render(request,"facultylogin.html")
def user_detail_view(request, user_id):
    

    user = CustomUser.objects.get(id=user_id)

    

    teaching_details = TeacherDetails.objects.filter(faculty=user)
    current_date = timezone.now().date()
    try:
        attendance = AttendanceMarkings.objects.filter(date=current_date, faculty_name=user)
        print("133",attendance)
    except AttendanceMarkings.DoesNotExist:
        attendance = None

    context = {
        'user': user,
        'teaching_details': teaching_details,
        'attendance': attendance,
    }

    return render(request, 'facultydetail.html', context)
def studentdetailview(request,user_id):
    user=CustomUser.objects.get(id=user_id)
    student_details=StudentDetails.objects.filter(student_name=user)
    context={
        'user':user,
        'student_details':student_details
    }
    return render(request,'studentdetail.html',context)
    
def studentattendance(request,user_id):
    if request.method == 'GET':
        semester_taught = request.GET.get('semester')
        semesters=int(semester_taught[-1])
        
        student_details = StudentDetails.objects.filter(student_semester=semesters)
        for i in student_details:
            print("here giving the i ",i.id)
        students = [{'id': detail.student_name.id, 'name': detail.student_name.name} for detail in student_details]
        print(students)
        
        
        
        context={
            'students': students,
            'user_id':user_id,
            'semesters':semesters,
        }
        
        return render(request, 'attendancemark.html', context)
@csrf_exempt
def submit_attendance(request):
    if request.method == 'POST':
        user_id = int(request.GET.get('user_id'))
        
        print("type of the user_id",type(user_id))
        try:
            request_data = json.loads(request.body)
            attendance_data = request_data
            print(attendance_data)

            if user_id and attendance_data:
                for data in attendance_data:
                    student_id = int(data.get('studentId'))
                    attendance_status = data.get('attendanceStatus')
                    date = data.get('date')
                    semester=data.get('semester')
                    student_name=CustomUser.objects.get(pk=student_id)
            
                    faculty_name=CustomUser.objects.get(pk=user_id)
                    
                    print("inside the block",student_name)
                    AttendanceMarkings.objects.create(
                        student_name=student_name,
                        faculty_name=faculty_name,
                        semester=semester,
                        attendance_status=attendance_status,
                        date=date
                    )

                return redirect(reverse('faculty_detail', kwargs={'user_id': user_id}))
    
            else:
                return JsonResponse({'error': 'Missing user_id or attendance data'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
def viewstudentattendance(request,user_id):
    
    student_name= CustomUser.objects.get(pk=user_id)
    print("12133122",student_name)
    attendance_mark=AttendanceMarkings.objects.get(student_name=student_name)
    
    print(attendance_mark.date)
    context={
            'attendance_mark':attendance_mark
        }
    return render(request,'studentattendance.html',context)