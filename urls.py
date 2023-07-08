from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.index,name='home.html'),
    path('home',views.index,name='home.html'),
    path('aboutus',views.about,name='aboutus.html'),
    path('login/',views.logins,name='login.html'),
    path('notification',views.notifications,name='notification'),
    path('reg',views.reg,name='reg.html'),
    path('terms',views.terms,name='terms.html'),
    path('college/',views.college_dashboard,name='college_dashboard.html'),
    path('student/',views.student_dashboard,name='student_dashboard.html'),
    path('adminn/',views.admin_dashboard,name='admin_dashboard.html'),
    path('logout',views.logouts,name='home.html'),
    path('forgetpass',views.forgetpass,name='forgot_password.html'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('college_profile',views.college_profile,name='college_profile.html'),
    path('admin_profile',views.admin_profile,name='admin_profile.html'),
    path('apply',views.apply,name='apply.html'),
    path('c_apply',views.c_apply,name='c_apply.html'),
    path('applydone',views.applydone,name='applydone.html'),
    path('college_register/', views.college_register, name='college_register'),
    path('student_register/', views.student_register, name='student_register'),
    path('college_list',views.college_list,name='college_list.html'),
    path('student_list/', views.student_list, name='student_list'),
    path("status",views.status,name="status"),
    path('ratings',views.ratings,name='ratings.html'),
    path('view_applicants',views.applicants,name='applicants'),
    path('get_available_courses/', views.get_available_courses, name='get_available_courses'),
    path('manage_course',views.manage_course,name='manage_course'),
    path('add_course/<int:college_id>/', views.add_course, name='add_course'),
    path('delete_course/<int:college_id>/', views.delete_course, name='delete_course'),
    path('tieup_status',views.tieup_status,name='tieup_status'),
    path('college_request',views.college_request,name='college_request'),
    path('add_notification',views.add_notification,name='add_notification'),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('viewall',views.viewall,name='viewall'),

]


