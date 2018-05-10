"""SIESWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from SIESWebApp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('try/', views.try1, name='try'),
    path('IT/', views.IT_about, name='IT_about'),
    
    path('Comp', views.Comp_about, name='Comp_about'),
    path('Comp_faculty', views.Comp_faculty, name='Comp_faculty'),
    path('Comp_student_development/', views.Comp_student_development, name='Comp_student_development'),
    
    path('Extc', views.Extc_about, name='Extc_about'),
    path('Extc_faculty', views.Extc_faculty, name='Extc_faculty'),
    path('Extc_student_development/', views.Extc_student_development, name='Extc_student_development'),
    path('Extc_department_activities/', views.Extc_deptartment_activities, name='Extc_department_activities'),
    
    path('Ppt', views.Ppt_about, name='Ppt_about'),
    path('Ppt_faculty', views.Ppt_faculty, name='Ppt_faculty'),
    path('Ppt_student_development/', views.Ppt_student_development, name='Ppt_student_development'),
    path('Ppt_department_activities/', views.Ppt_deptrtment_activities, name='Ppt_department_activities'),
    
    path('Mech_about/', views.Mech_about, name='Mech_about'),
    path('Mech_achievement/', views.Mech_achievement, name='Mech_achievement'),
    path('Mech__dept/', views.Mech_department, name='Mech_department'),
    path('Mech_fac/', views.Mech_faculty, name='Mech_faculty'),
    path('Mech_activity/', views.Mech_student_activities, name='Mech_student_activities'),
    path('Mech_dept_activity/', views.Mech_department_activities, name='Mech_department_activities'),

    path('HAS/', views.HAS_about, name='HAS_about'),
    path('HAS__dept/', views.HAS_department, name='HAS_department'),
    path('HAS_dept_activity/', views.HAS_department_activities, name='HAS_department_activities'),
    path('HAS_fac/', views.HAS_faculty, name='HAS_faculty'),
    path('HAS_achievement/', views.HAS_achievement, name='HAS_achievement'),
    ]