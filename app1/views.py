from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.

# to load homepage
def load_home(request):
    return render(request,'user/home.html')

# to load coursepage
def course_page(request):
    return render(request,'admin/course.html')

# to add course
def add_course(request):
    if request.method == 'POST':
        coursename=request.POST['cname']
        coursefees=request.POST['cfee']
        data = courses_model(course_name=coursename,course_fees=coursefees)
        data.save()
    return redirect('course_page')

# to load signup
def sign_page(request):
    courses=courses_model.objects.all()
    context={'courses':courses}
    return render(request,'user/signup.html',context)

# to load login
def loogin(request):
    return render(request,'user/login.html')

# to signup
def add_teacher(request):
    if request.method == 'POST':
        fname=request.POST['tfname']
        lname=request.POST['tlname']
        uname=request.POST['tuname']
        mail=request.POST['tmail']
        address=request.POST['taddress']
        gender=request.POST['tgender']
        select=request.POST['select']
        password=request.POST['tpassword']
        cpassword=request.POST['tcpassword']
        if request.FILES.get('file') is not None:
            photo = request.FILES['file']
            print("photo added")
        else :
            photo = '/static/images/blank-profile-picture-973460_640.png'
            print("default photo added")
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                return redirect('sign_page')
                print("username alreadt taken")
            elif User.objects.filter(email=mail).exists():
                return redirect('sign_page')
                print("mail already taken")
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    email=mail,
                    password=password)
                user.save()
                
                u=User.objects.get(id=user.id)
                c=courses_model.objects.get(id=select)
                addteach=teacher_model(address=address,gender=gender,image=photo,user=u,course=c)
                addteach.save()
                print("create successfully")
        else:
            return redirect('sign_page')
            print("pasword didnt match")
        return redirect('loogin')
    else:
        return redirect('sign_page')  

# to login
def user_login(request):
    if request.method == 'POST':
        uname=request.POST['tuname']
        password=request.POST['tpassword']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            if user.is_staff:
                return redirect('load_adminhome')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('load_staffhome')
        else:
            return redirect('loogin')
    else:
        return redirect('loogin')

# to logout
def logout(request):
    auth.logout(request)
    return redirect('load_home')

# to load_adminhome
def load_adminhome(request):
    return render(request,'admin/adminhome.html')

# to load staffhome
def load_staffhome(request):
    return render(request,'user/staffhome.html')

# to  load_addstudent
def load_addstudent(request):
    courses=courses_model.objects.all()
    context={'courses':courses}
    return render(request,'admin/addstudent.html',context)

# to add student
def addstudent(request):
    if request.method == 'POST':
        name=request.POST['sname']
        age=request.POST['sage']
        gender=request.POST['sgender']
        select=request.POST['select']
        course=courses_model.objects.get(id=select)
        data = student_model(name=name,age=age,gender=gender,course=course)
        data.save()
        return redirect('load_addstudent')

# to show student details
def StudentDetails(request):
    student_detail = student_model.objects.all()
    return render(request,'admin/showstudent.html',{'student':student_detail})

# to show teacher details
def TeachertDetails(request):
    teacher_detail = teacher_model.objects.all()
    return render(request,'admin/showteacher.html',{'teacher':teacher_detail})

# to show teacher personal profile
def teacherprofileview(request):
    teacher_detail = teacher_model.objects.get(user=request.user)
    return render(request,'user/teacherprofile.html',{'teacher':teacher_detail})

# to load teacher profile edit
# def load_edit(request,pk):
#     details=teacher_model.objects.get(id=pk)
#     return render(request,'user/editteacherprofile.html',{'details':details})

# to edit teacher personal profile
# def edit_teacher_profile(request,pk):
#     if request.method=='POST':
#         data = teacher_model.objects.get(id=pk)
#         data.user.first_name = request.POST.get('tfname')
#         data.user.last_name = request.POST.get('tlname')
#         data.user.email = request.POST.get('tmail')
#         data.address = request.POST.get('taddress')
#         data.save()
#         return redirect('teacherprofileview')
#     return render(request,'user/editteacherprofile.html')

# to show teacher personal profile
# def edit_teacherprofileview(request):
#     teacher_detail = teacher_model.objects.get(user=request.user)
#     return render(request,'user/teacherprofile.html',{'teacher':teacher_detail})

def load_edit(request):
    teacher=teacher_model.objects.get(user=request.user)
    return render(request,"user/editteacherprofile.html",{'edit':teacher})


def edit_teacher_profile(request):
    if request.method=='POST':
        tdata = teacher_model.objects.get(Teacher=request.user)
        tdata.user.first_name = request.POST.get('tfname')
        tdata.user.last_name = request.POST.get('tlname')
        tdata.user.email = request.POST.get('tmail')
        tdata.address = request.POST.get('taddress')
        tdata.save()
        tdata.user.save()
        return redirect('teacherprofileview')
    return render(request, 'user/editprofile.html')

# to delete student 
def del_student(request,pk):
    std = student_model.objects.get(id=pk)
    std.delete()
    return redirect('StudentDetails')

# to delete teacher 
def del_teacher(request,pk):
    tcr = teacher_model.objects.get(id=pk)
    tcr.delete()
    return redirect('TeachertDetails')

# to show course
def Course_Details(request):
        crs=courses_model.objects.all()
        return render(request,'admin/showcourse.html',{'crs':crs})


                