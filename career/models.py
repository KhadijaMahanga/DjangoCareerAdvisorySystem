# this document contains the classes needed to run the core browsing and profile managment features of the application
# 15 September 2014
# Career Study Advisor

from django.db import models
from django import forms
from django.contrib.auth.models import User, UserManager

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

GENDER_CHOICES = (
  ('Female','Female'),('Male','Male'),
)
YOU_CHOICES = (
  ('student','Student'),('advisor','Advisor'),
)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class UserProfile(models.Model):# this class contains the student users of the application
    user=models.OneToOneField(User)
    subscriber=models.BooleanField(default=False)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    school=models.CharField(max_length=200, null=True)
    gender=models.CharField(max_length=20, choices=GENDER_CHOICES)
    dateofbirth=models.DateField(blank=True, null=True)
    grade=models.CharField(max_length=200, null=True)

    def __unicode__(self):
	return self.user.username

    def subscribeToNewsletter():
        self.subscriber= True



class AdvisorProfile(models.Model):# this class contains the student users of the application
    user=models.OneToOneField(User)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    gender=models.CharField(max_length=20, choices=GENDER_CHOICES)
    dateofbirth=models.DateField(blank=True, null=True)

    def __unicode__(self):
	return self.user.username


class Institution(models.Model): # this class contains information information about the institutions and their contact details
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=10000)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    tel=models.CharField(max_length=200)
    weblink=models.URLField()
    picture = models.URLField()
    def __unicode__(self):
	return self.name
    
class StudyArea(models.Model):# this class contains the specific study areas/ career fields
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=50000)
    picture = models.URLField()
    def __unicode__(self):
	return self.title
    def getDescription():
        return self.description


class Programme(models.Model):# this class contains the specific courses that are held at a specific institution
    programmeName=models.CharField(max_length=200)
    description=models.CharField(max_length=50000)
    minimumRequirements=models.CharField(max_length=10000)
    institutionOffered=models.ForeignKey(Institution)
    studyAreaOffered=models.ForeignKey(StudyArea)
    applicationDeadline=models.DateTimeField(auto_now_add=False)
    weblink=models.URLField()
    def __unicode__(self):
	return self.programmeName

class Reminder (models.Model):# this class is used to add application closing date reminders to users
    username=models.CharField(max_length=200)
    dateCourse=models.CharField(max_length=200)
    def __unicode__(self):
	return (self.username+" "+self.dateCourse)
        

