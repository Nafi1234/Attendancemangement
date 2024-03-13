from django.db import models
from myadmin.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Year(models.Model):
    semesters_no = models.IntegerField()
    subject = models.CharField(max_length=100)
    def __str__(self):
        return f"Semester {self.semesters_no}"

class TeacherDetails(models.Model):
    faculty = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    semester_taught = models.ForeignKey(Year, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.faculty.name} teaches {self.semester_taught}"
class StudentDetails(models.Model):
    student_name=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    student_semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    def __str__(self):
        return f"{self.student_name} studies in {self.student_semester}"
class AttendanceMarkings(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    student_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student_attendancemarkings')
    faculty_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='faculty_attendancemarkings')
    date = models.DateField()
    semester = models.IntegerField()
    attendance_status = models.CharField(max_length=7, choices=ATTENDANCE_CHOICES)
