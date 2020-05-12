from __future__ import unicode_literals
from django.contrib import admin
from resume.models import Person, Education, ProjectOrJob, TechnicalSkills,PositionOfResponsibilites,Achievements,Extracurriculars,Academics,AreaOfInterest
# Register your models here.
admin.site.register(Education)
admin.site.register(Person)
admin.site.register(ProjectOrJob)
admin.site.register(TechnicalSkills)
admin.site.register(PositionOfResponsibilites)
admin.site.register(Achievements)
admin.site.register(Academics)
admin.site.register(AreaOfInterest)
admin.site.register(Extracurriculars)
