from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_college=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    status=models.CharField(max_length=50,default='')
    photo = models.ImageField(upload_to='media/',default='default.jpg')
    phone = models.CharField(max_length=20,default='')
    

class Student(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    username=models.CharField(max_length=100,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    father_name=models.CharField(max_length=100,null=True)
    mother_name=models.CharField(max_length=100,null=True)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=1,choices=(('M','Male'),('F','Female')))
    phone_number=models.CharField(max_length=20)
    alt_number=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    sslc_percentage=models.DecimalField(max_digits=5,decimal_places=2)
    sslc_school=models.CharField(max_length=100,null=True)
    puc_percentage=models.DecimalField(max_digits=5,decimal_places=2)
    puc_college=models.CharField(max_length=100,null=True)
    college=models.CharField(max_length=100,default="empty")
    selected_course=models.CharField(max_length=100,default="empty")
    photo = models.ImageField(upload_to='media/',default='default.jpg')
    
    
    def __str__(self):
        return self.first_name

class College(models.Model):
    clg=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    username=models.CharField(max_length=100,null=True)
    college_name=models.CharField(max_length=100,null=True)
    place=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    college_strength=models.CharField(max_length=5,null=True)
    inaugration_date=models.DateField()
    naac_grade=models.CharField(max_length=3,null=True)
    principal_phone=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    courses_available = models.TextField(max_length=20,blank=True)
    photo = models.ImageField(upload_to='media/',default='default.jpg')
    def __str__(self):
        return self.college_name
    
class Review(models.Model):
    username=models.CharField(max_length=100,null=True)
    rating=models.CharField(max_length=100,null=True)
    feedback=models.CharField(max_length=100,null=True)
    timestamp=models.DateField(default=timezone.now)
    def __str__(self):
        return self.username
    
class Application(models.Model):
    std=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL,related_name='std')
    applied_by=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='applied_by')
    applied_to=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='applied_to')
    status=models.BooleanField(default=False)
    rej=models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

class Notification(models.Model):
    message = models.TextField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message
