from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# to add courses
class courses_model(models.Model):
    course_name=models.CharField(max_length=255)
    course_fees=models.IntegerField()

# to add teacher
class teacher_model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(courses_model,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    gender=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')

# to add student
class student_model(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(max_length=255)
    course=models.ForeignKey(courses_model,on_delete=models.CASCADE,null=True)
