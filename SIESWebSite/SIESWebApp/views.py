from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def try1(request):
    return render(request, 'try.html')

############ IT Department#############
#######################################
def IT_about(request):
    return render(request, 'IT/About_IT.html')

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