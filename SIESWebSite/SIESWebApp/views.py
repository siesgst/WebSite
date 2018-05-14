from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def try1(request):
    return render(request, 'try.html')

############ IT Department#############
#######################################
def IT_about(request):
    return render(request, 'IT/About_IT.html')
def IT_faculty(request):
    return render(request, 'IT/IT_faculty.html')

######### Computer Department##########
#######################################
def Comp_about(request):
    return render(request, 'Comp/About_Comp.html')

def Comp_student_development(request):
    return render(request, 'Comp/Comp_student_development.html')

def Comp_faculty(request):
    return render(request, 'Comp/Comp_faculty.html')


########### EXTC Department############
#######################################
def Extc_about(request):
    return render(request, 'Extc/About_Extc.html')

def Extc_deptartment_activities(request):
    return render(request, 'Extc/Extc_department_activities.html')

def Extc_student_development(request):
    return render(request, 'Extc/Extc_student_development.html')

def Extc_faculty(request):
    return render(request, 'Extc/Extc_faculty.html')


############ PPT Department############
#######################################
def Ppt_about(request):
    return render(request, 'Ppt/About_PPT.html')

def Ppt_deptrtment_activities(request):
    return render(request, 'Ppt/Ppt_department_activities.html')

def Ppt_student_development(request):
    return render(request, 'Ppt/Ppt_student_development.html')

def Ppt_faculty(request):
    return render(request, 'Ppt/Ppt_faculty.html')


####### Mechanical Department #########
#######################################
def Mech_about(request):
    return render(request, 'Mech/About_Mech.html')

def Mech_achievement(request):
    return render(request, 'Mech/Mech_achievement.html')

def Mech_department(request):
    return render(request, 'Mech/Mech_department.html')

def Mech_faculty(request):
    return render(request, 'Mech/Mech_faculty.html')

def Mech_student_activities(request):
    return render(request, 'Mech/Mech_student_activities.html')

def Mech_department_activities(request):
    return render(request, 'Mech/Mech_department_activities.html')


########### HSA Department ############
#######################################
def HAS_about(request):
    return render(request, 'HAS/About_HAS.html')

def HAS_department(request):
    return render(request, 'HAS/HAS_department.html')

def HAS_department_activities(request):
    return render(request, 'HAS/HAS_department_activities.html')

def HAS_faculty(request):
    return render(request, 'HAS/HAS_faculty.html')

def HAS_achievement(request):
    return render(request, 'HAS/HAS_achievement.html')


############# Admission ###############
#######################################
def Admission( request):
    return render(request, 'Admission/Admission.html')
def Brochure( request):
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Brochure.pdf'
    path = base_url + '\\Admission\\' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')

def Feestructure( request):    
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Computtation_of_Fee_Engineering_2018-19.pdf'
    path = base_url + '\\MandatoryDisclosure\\' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')


############## Mandatory Disclosure ###############
###################################################
def Mandatory_disclosure_documents(request):
    return render(request, 'MandatoryDisclosure/Mandatory_Disclosure.html')

def Mandatory_disclosure( request):    
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'mandatory_disclosure.pdf'
    path = base_url + '\\MandatoryDisclosure\\' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')

def AICTE_approval( request):    
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'EOA_Report_2017-18.pdf'
    path = base_url + '\\MandatoryDisclosure\\' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')



############## Research ###############
#######################################
def Research_Grants(request):
    return render(request, 'Research/Research_Grants.html')


############## Alumni ###############
#######################################
def Alumni(request):
    return render(request, 'Alumni/Alumni.html')

############# Placement ##############
#######################################
def Placement_about(request):
    return render(request, 'Placement/Placement_department.html')
def Training(request):
    return render(request, 'Placement/Training.html')
def Placement(request):
    return render(request, 'Placement/Placement.html')
def Higher_Education(request):
    return render(request, 'Placement/Higher_Education.html')

############## About Us ###############
#######################################
def Anti_ragging_committee(request):
    return render(request, 'About_us/Anti_ragging_committee.html')

def Core_values(request):
    return render(request, 'About_us/Core_values.html')

def Internal_complaint_committee(request):
    return render(request, 'About_us/Internal_complaint_committee.html')

def Iqac(request):
    return render(request, 'About_us/Iqac.html')

def Managing_committee(request):
    return render(request, 'About_us/Managing_committee.html')

def Organisation_and_governance(request):
    return render(request, 'About_us/Organisation_and_governance.html')

def Overview(request):
    return render(request, 'About_us/Overview.html')

def The_principal(request):
    return render(request, 'About_us/The_principal.html')

def Vision_and_mission(request):
    return render(request, 'About_us/Vision_and_mission.html')

def Woman_dev_cell(request):
    return render(request, 'About_us/Woman_dev_cell.html')

def Strategic_plan(request):
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Strategic_plan.pdf'
    path = base_url + '\\About_us\\' + filename
    #path = base_url + '/About_us/' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')

def Iqac_minutes_of_meetings(request):
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Iqac_minutes_of_meetings.pdf'
    path = base_url + '\\About_us\\' + filename
    #path = base_url + '/About_us/' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')

def Iqac_formation_report(request):
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Iqac_formation_report.pdf'
    path = base_url + '\\About_us\\' + filename
    #path = base_url + '/About_us/' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')

def Anti_ragging(request):
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Anti_ragging.pdf'
    path = base_url + '\\About_us\\' + filename
    #path = base_url + '/About_us/' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')
  
def Core_values_img(request):
    from django.conf import settings
    #base_url = 'file://' + settings.STATIC_ROOT
    base_url = settings.STATIC_ROOT
    filename = 'Core_values_img.pdf'
    path = base_url + '\\About_us\\' + filename
    #path = base_url + '/About_us/' + filename
    data = open(path, 'rb').read()
    return HttpResponse(data, content_type='application/pdf')


############# Amenities ##############
#######################################
def Aakash_project_labs(request):
    return render(request, 'Amenities/Aakash_project_labs.html')
def Auditorium_and_halls(request):
    return render(request, 'Amenities/Auditorium_and_halls.html')
def Computer_centre(request):
    return render(request, 'Amenities/Computer_centre.html')
def Divyangan(request):
    return render(request, 'Amenities/Divyangan.html')
def Eyantra(request):
    return render(request, 'Amenities/Eyantra.html')
def General_laboratories(request):
    return render(request, 'Amenities/General_laboratories.html')
def Iitbombay(request):
    return render(request, 'Amenities/Iitbombay.html')
def Intranet(request):
    return render(request, 'Amenities/Intranet.html')
def Library(request):
    return render(request, 'Amenities/Library.html')
def Miscellaneous(request):
    return render(request, 'Amenities/Miscellaneous.html')
def Amenities_department(request):
    return render(request, 'Amenities/Amenities_department.html')

############# ####### Contact_us  ####################
####################################### ##############
def Contact_us(request):
    return render(request, 'Contact_us/Contact_us.html')

############# ####### Support  ####################
####################################### ##############
def Admin_office(request):
    return render(request, 'Support/Admin_office.html')
def Exam_cell(request):
    return render(request, 'Support/Exam_cell.html')
def Nonteaching_staff(request):
    return render(request, 'Support/Nonteaching_staff.html')
def About_support(request):
    return render(request, 'Support/About_support.html')