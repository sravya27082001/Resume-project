from django.utils import timezone
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    roll_no=models.CharField(max_length=15)
    email=models.EmailField()
    college_mail=models.EmailField()
    github=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)

    def full_name(self):
        return " ".join([self.first_name,self.last_name])



class Education(models.Model):
    DEGREE_CHOICES=(
        ('1', 'Phd'),
        ('2','Mtech/MA/MSc/MCom/MBA'),
        ('3','BE/Btech/BA/BSc/BCom'),
        ('4', 'High School')
    )
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    degree=models.CharField(max_length=1,choices=DEGREE_CHOICES)
    passing_year=models.DateField()
    institute=models.CharField(max_length=100)
    percentage=models.CharField(max_length=5)



class ProjectOrJob(models.Model):
    WORK_CHOICES = (
        ('J', 'Job'),
        ('P', 'Project')
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    work = models.CharField(max_length=1, choices=WORK_CHOICES)
    title=models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class TechnicalSkills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_detail = models.TextField()

class PositionOfResponsibilites(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    resposibilities_taken = models.TextField()


class Achievements(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    achievements_detail = models.TextField()

class Academics(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    academic_detail = models.TextField()

class AreaOfInterest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    area_of_interest_detail = models.TextField()

class Extracurriculars(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    extracurriculars_detail = models.TextField()
