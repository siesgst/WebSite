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
    path('IT_faculty/', views.IT_faculty, name='IT_faculty'),
    
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
    path('Mech_department/', views.Mech_department, name='Mech_department'),
    path('Mech_faculty/', views.Mech_faculty, name='Mech_faculty'),
    path('Mech_activity/', views.Mech_student_activities, name='Mech_student_activities'),
    path('Mech_dept_activity/', views.Mech_department_activities, name='Mech_department_activities'),

    path('HAS/', views.HAS_about, name='HAS_about'),
    path('HAS__dept/', views.HAS_department, name='HAS_department'),
    path('HAS_dept_activity/', views.HAS_department_activities, name='HAS_department_activities'),
    path('HAS_fac/', views.HAS_faculty, name='HAS_faculty'),
    path('HAS_achievement/', views.HAS_achievement, name='HAS_achievement'),
    
    path('Admission/', views.Admission, name='Admission'),
    path('Brochure/', views.Brochure, name='Brochure'),
    path('Feestructure/', views.Feestructure, name='Feestructure'),
    
    path('Research_Grants/', views.Research_Grants, name='Research_Grants'),
    path('Alumni/', views.Alumni, name='Alumni'),
    
    
    path('Placement_about/', views.Placement_about, name='Placement_about'),
    path('Training/', views.Training, name='Training'),
    path('Placement/', views.Placement, name='Placement'),
    path('Higher_education/', views.Higher_Education, name='Higher_education'), 
    
    path('Anti_ragging_committee', views.Anti_ragging_committee, name='Anti_ragging_committee'),
    path('Core_values', views.Core_values, name='Core_values'),
    path('Internal_complaint_committee', views.Internal_complaint_committee, name='Internal_complaint_committee'),
    path('Iqac', views.Iqac, name='Iqac'),
    path('Managing_committee', views.Managing_committee, name='Managing_committee'),
    path('Organisation_and_governance', views.Organisation_and_governance, name='Organisation_and_governance'),
    path('Overview', views.Overview, name='Overview'),
    path('The_principal', views.The_principal, name='The_principal'),
    path('Vision_and_mission', views.Vision_and_mission, name='Vision_and_mission'),
    path('Woman_dev_cell', views.Woman_dev_cell, name='Woman_dev_cell'),
    path('Strategic_plan', views.Strategic_plan, name='Strategic_plan'),
    path('Iqac_minutes_of_meetings', views.Iqac_minutes_of_meetings, name='Iqac_minutes_of_meetings'),
    path('Iqac_formation_report', views.Iqac_formation_report, name='Iqac_formation_report'),
    path('Anti_ragging', views.Anti_ragging, name='Anti_ragging'),
    path('Core_values_img', views.Core_values_img, name='Core_values_img'), 
    
    
    path('Aakash_project_labs/', views.Aakash_project_labs, name='Aakash_project_labs'),
    path('Amenities_department/', views.Amenities_department, name='Amenities_department'),
    path('Auditorium_and_halls/', views.Auditorium_and_halls, name='Auditorium_and_halls'),
    path('Computer_centre/', views.Computer_centre, name='Computer_centre'),
    path('Divyangan/', views.Divyangan, name='Divyangan'),
    path('Eyantra/', views.Eyantra, name='Eyantra'),
    path('General_laboratories/', views.General_laboratories, name='General_laboratories'),
    path('Iitbombay/', views.Iitbombay, name='Iitbombay'),
    path('Intranet/', views.Intranet, name='Intranet'),
    path('Library/', views.Library, name='Library'),
    path('Miscellaneous/', views.Miscellaneous, name='Miscellaneous'),
    
    path('Contact_us/', views.Contact_us, name='Contact_us'),
    
    
    path('Mandatory_disclosure_documents/', views.Mandatory_disclosure_documents, name='Mandatory_disclosure_documents'),
    path('Mandatory_disclosure/', views.Mandatory_disclosure, name='Mandatory_disclosure'),
    path('AICTE_approval/', views.AICTE_approval, name='AICTE_approval'),
    
    
     
    path('About_support/', views.About_support, name='About_support'),
    path('Admin_office/', views.Admin_office, name='Admin_office'),
    path('Exam_cell/', views.Exam_cell, name='Exam_cell'),
    path('Nonteaching_staff/', views.Nonteaching_staff, name='Nonteaching_staff'),
    ]