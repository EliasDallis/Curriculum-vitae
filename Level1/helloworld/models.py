from django.db import models
from Level1 import settings
from django.utils import timezone

# Create your models here.
class PreviousFirm (models.Model):
    job_company = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self):
        return self.job_company

class PreviousTitle(models.Model): 
    title_company = models.ForeignKey(PreviousFirm, on_delete=models.CASCADE, related_name='firms')
    job_title = models.CharField(max_length=50, unique=False)
    start_date = models.DateField()
    end_date = models.DateField()
    job_desc = models.TextField()

    def __str__(self):
        return str(self.job_title)

class CurrentObjective(models.Model):
    current_obj_text = models.TextField()
    def __str__(self):
        return str("Objective")

class Education(models.Model):
    course_name = models.CharField(max_length=64)
    course_provider = models.CharField(max_length=64)
    course_grade = models.CharField(max_length=16)
    course_start = models.DateField()
    course_end = models.DateField()
    course_desc = models.TextField()
    def __str__(self):
        return self.course_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=64)
    skill_desc = models.TextField()
    def __str__(self):
        return self.skill_name

class Biography(models.Model):
    bio_para1 = models.TextField()
    bio_para2 = models.TextField()
    bio_para3 = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return str((self.create_date))

class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    display = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.name)+' - ' +str(self.time)[:16])

class Portfolio(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    def __str__(self):
        return (self.title)