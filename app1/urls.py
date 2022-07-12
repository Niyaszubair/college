from django.urls import path
from . import views

urlpatterns = [
    path('',views.load_home,name='load_home'),
    path('course_page',views.course_page,name='course_page'),
    path('add_course/',views.add_course,name='add_course'),
    path('sign_page/',views.sign_page,name='sign_page'),
    path('loogin/',views.loogin,name='loogin'),
    path('user_login/',views.user_login,name='user_login'),
    path('add_teacher/',views.add_teacher,name='add_teacher'),
    path('load_adminhome/',views.load_adminhome,name='load_adminhome'),
    path('load_staffhome/',views.load_staffhome,name='load_staffhome'),
    path('logout/',views.logout,name='logout'),
    path('load_addstudent/',views.load_addstudent,name='load_addstudent'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('StudentDetails/',views.StudentDetails,name='StudentDetails'),
    path('TeachertDetails/',views.TeachertDetails,name='TeachertDetails'),
    path('teacherprofileview/',views.teacherprofileview,name='teacherprofileview'),
    path('edit_teacher_profile/',views.edit_teacher_profile,name='edit_teacher_profile'),
    path('load_edit/',views.load_edit,name='load_edit'),
    # path('load_edit/<int:pk>',views.load_edit,name='load_edit'),

    # path('edit_teacher_profile/<int:pk>',views.edit_teacher_profile,name='edit_teacher_profile'),
    path('del_student/<int:pk>',views.del_student,name='del_student'),
    path('del_teacher/<int:pk>',views.del_teacher,name='del_teacher'),
    path('Course_Details/',views.Course_Details,name='Course_Details'),
]
