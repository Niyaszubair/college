from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(courses_model)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','course_name','course_fees')

@admin.register(teacher_model)
class teacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','user','course','address','gender','image')

@admin.register(student_model)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','name','age','gender','course')