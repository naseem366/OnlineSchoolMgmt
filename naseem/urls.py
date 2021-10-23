
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [


    path('',views.home ,name='home'),
   
    path('addAttendance/', views.addAttendance,name='addAttendance'),
   
    path('addMarks/', views.addMarks,name='addMarks'),
 
    path('addNotice/', views.addNotice,name='addNotice'),
 
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registerPage,name='register'),
    path('upload/', views.uploadPage,name='upload'),
    path('read_from_database/<int:applicant_id>',views.resume,name='read_from_database'),
    path('read_files/',views.export_auto_doc,name='read_files'),


]