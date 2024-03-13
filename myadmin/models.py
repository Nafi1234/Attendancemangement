from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name,user_type,password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name, user_type=user_type,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    name=models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USER_TYPES=[
        ('S','Student'),
        ('F','Faculty')
    ]
    user_type=models.CharField(max_length=1,choices=USER_TYPES)
    objects = CustomUserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','user_type']

    def __str__(self):
        return self.email

class Semesterss(models.Model):
    semester_no = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"Semester {self.semester_no}"

class FacultyDetails(models.Model):
    faculty = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    semester_taught = models.ForeignKey(Semesterss, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty.name} teaches {self.semester_taught}"