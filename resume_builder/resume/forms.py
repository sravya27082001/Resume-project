from django import forms
from .models import Person, Education, ProjectOrJob, TechnicalSkills,PositionOfResponsibilites,Achievements,Extracurriculars,Academics,AreaOfInterest


class PersonForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = "__all__"

        widgets = {
            'first_name': forms.TextInput(attrs={'title': 'First Name'}),
            'last_name': forms.TextInput(attrs={'title': 'Last Name'}),
            'roll_no': forms.TextInput(attrs={'title': 'Roll Number'}),
            'email': forms.EmailInput(attrs={'title': 'Email'}),
            'college_mail': forms.EmailInput(attrs={'title': 'Email'}),
            'github': forms.URLInput(attrs={'title': 'Github'}),
            'linkedin': forms.URLInput(attrs={'title': 'LinkedIn'})
        }

class EducationForm(forms.ModelForm):

    class Meta:
         model=Education
         fields=('degree','passing_year','institute','percentage')

         widgets={
              'degree': forms.Select(attrs={'title':'Degree'}),
              'passing_year': forms.DateInput(attrs={'title': 'Passing Date'}),
              'institute':forms.TextInput(attrs={'title': 'Institute'}),
              'percentage':forms.TextInput(attrs={'title': 'Percntage/CGPA'})
         }


class ProjectOrJobForm(forms.ModelForm):

    class Meta:
        model = ProjectOrJob
        fields = ('work', 'title', 'start_date', 'end_date', 'description')
        widgets = {

            'work': forms.Select(attrs={'title': 'Work'}),
            'title': forms.TextInput(attrs={'title': 'Title'}),
            'start_date': forms.DateInput(attrs={'title': 'Start Date'}),
            'end_date': forms.DateInput(attrs={'title': 'End Date'}),
            'description': forms.Textarea(attrs={'title': 'Description'})
       }


class TechnicalSkillsForm(forms.ModelForm):

    class Meta:
        model = TechnicalSkills
        fields = ('skill_detail',)
        widgets = {

            'skill_detail': forms.Textarea(attrs={'title': 'Technical Skills'})
        }

class PositionOfResponsibilitesForm(forms.ModelForm):

    class Meta:
        model=PositionOfResponsibilites
        fields = ('resposibilities_taken',)

        widgets={
            'resposibilities_taken': forms.Textarea(attrs={'title': 'Responsibilities Taken'})
        }


class AchievementsForm(forms.ModelForm):
    class Meta:
        model=Achievements
        fields=('achievements_detail',)

        widgets={
            'achievements_detail': forms.Textarea(attrs={'title': 'Achievements'})
        }

class AcademicsForm(forms.ModelForm):

    class Meta:
        model = Academics
        fields = ('academic_detail',)
        widgets = {

            'academic_detail': forms.Textarea(attrs={'title': 'Academics'})
        }

class AreaOfInterestForm(forms.ModelForm):

    class Meta:
        model = AreaOfInterest
        fields = ('area_of_interest_detail',)
        widgets = {

            'area_of_interest_detail': forms.Textarea(attrs={'title': 'Area Of Interest'})
        }

class ExtracurricularsForm(forms.ModelForm):

    class Meta:
        model=Extracurriculars
        fields=('extracurriculars_detail',)
        widgets = {

            'extracurriculars_detail': forms.Textarea(attrs={'title': 'Extracurriculars'})
        }
