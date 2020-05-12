from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Person, Education, ProjectOrJob, TechnicalSkills,PositionOfResponsibilites,Achievements,Academics,AreaOfInterest,Extracurriculars
from resume.forms import PersonForm, EducationForm, ProjectOrJobForm, TechnicalSkillsForm, PositionOfResponsibilitesForm, AchievementsForm, AcademicsForm, AreaOfInterestForm,ExtracurricularsForm

def index(request):
    return render(request,'resume/index.html')

def resumeFill(request):


    if request.method=='POST':
        personform = PersonForm(request.POST)
        educationform = EducationForm(request.POST)
        projectOrJobform = ProjectOrJobForm(request.POST)
        technicalSkillsform = TechnicalSkillsForm(request.POST)
        positionOfResponsibilitesform=PositionOfResponsibilitesForm(request.POST)
        achievementsform=AchievementsForm(request.POST)
        academicsform = AcademicsForm(request.POST)
        areaOfInterestform = AreaOfInterestForm(request.POST)
        extracurricularsform=ExtracurricularsForm(request.POST)
        print(personform.errors)
        print(educationform.errors)
        print(projectOrJobform.errors)
        print(technicalSkillsform.errors)
        print(positionOfResponsibilitesform.errors)
        print(achievementsform.errors)
        print(academicsform.errors)
        print(areaOfInterestform.errors)
        print(extracurricularsform.errors)

        if personform.is_valid() and technicalSkillsform.is_valid() and educationform.is_valid() and projectOrJobform.is_valid() and positionOfResponsibilitesform.is_valid() and achievementsform.is_valid() and academicsform.is_valid() and areaOfInterestform.is_valid() and extracurricularsform.is_valid():

            print("all validations passed")
            P=personform.save()
            P.save()
            T=technicalSkillsform.save(commit=False)
            T.person=P
            T.save()
            Ed=educationform.save(commit=False)
            Ed.person=P
            Ed.save()
            PJ=projectOrJobform.save(commit=False)
            PJ.person=P
            PJ.save()
            POR=positionOfResponsibilitesform.save(commit=False)
            POR.person=P
            POR.save()
            A=achievementsform.save(commit=False)
            A.person=P
            A.save()
            Ac=academicsform.save(commit=False)
            Ac.person=P
            Ac.save()
            AI=areaOfInterestform.save(commit=False)
            AI.person=P
            AI.save()
            E=extracurricularsform.save(commit=False)
            E.person=P
            E.save()

            return index(request)

    else:
        personform = PersonForm()
        educationform = EducationForm()
        projectOrJobform = ProjectOrJobForm()
        technicalSkillsform = TechnicalSkillsForm()
        positionOfResponsibilitesform=PositionOfResponsibilitesForm()
        achievementsform=AchievementsForm()
        academicsform = AcademicsForm()
        areaOfInterestform = AreaOfInterestForm()
        extracurricularsform=ExtracurricularsForm()

    context = {
        'personform':personform,
        'educationform':educationform,
        'projectOrJobform':projectOrJobform,
        'technicalSkillsform':technicalSkillsform,
        'positionOfResponsibilitesform':positionOfResponsibilitesform,
        'achievementsform':achievementsform,
        'academicsform':academicsform,
        'areaOfInterestform':areaOfInterestform,
        'extracurricularsform':extracurricularsform
    }

    return render(request,'resume/resume_fill.html',context)

def resumeView(request):
    persons=Person.objects.all()
    education=Education.objects.all()
    return render(request,'resume/resume_view.html',{'persons':persons,
    'education':education})
