# This document contains the classes needed for the quiz sub-application
# 15 September 2014
# Career Study Advisor

from django.db import models
from django import forms
from django.contrib.auth.models import User, UserManager
from career.models import UserProfile, StudyArea


class Quiz(models.Model):  
    result=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    student= models.ForeignKey(UserProfile)
    def getQuizResult(self):
        return self.result
    def setResult(self,res):
        self.result=res
    def calculateQuizResultPartOne(self,arrayL):# this mthod determines the personality type 
	Realistic=0
        Investigative=0
	Artistic=0
	Social=0
	Enterprising=0
	Conventional=0
	# counts the number of choices corresponding to a personality type
	for i in arrayL:
	    if i=="Realistic":
		Realistic+=1
	    elif i=="Investigative":
		Investigative+=1
	    elif i=="Artistic":
		Artistic+=1
	    elif i=="Social":
		Social+=1
	    elif i=="Enterprising":
		Enterprising+=1
            elif i=="Conventional":
		Conventional+=1
	
	# calculate which option has the most and send it to the set Result method
	highest=""
        highestNum=0
	if Realistic>highestNum:
            highest="Realistic"
	    highestNum=Realistic
	if Investigative>highestNum:
            highest="Investigative"
	    highestNum=Investigative
	if Artistic>highestNum:
            highest="Artistic"
	    highestNum=Artistic
	if Social>highestNum:
            highest="Social"
	    highestNum=Social
	if Enterprising>highestNum:
            highest="Enterprising"
	    highestNum=Enterprising
	if Conventional>highestNum:
            highest="Conventional"
	    highestNum=Conventional

	self.setResult(highest)

class HarmonType(models.Model):# this class contains the main personality types as specified by Holland
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=50000)
    def __unicode__(self):
	return self.name
    def getName(self):
        return self.name


class Question(models.Model):
    question_text=models.CharField(max_length=1000)
    def __str__(self):
        return self.question_text


class QuestionPartOne(Question):# questions of this class form part of the first half of the quiz
    questionNumber=models.IntegerField(default=0)

class QuestionPartTwo(Question):# questions of this class form part of the second half of the quiz
    PartTwoHarmonType= models.ForeignKey(HarmonType)
    harmonTypeText=models.CharField(max_length=200)
    
  
class Choice(models.Model):
    choice_text=models.CharField(max_length=500)
    def __str__(self):
        return self.choice_text

class ChoicePartOne(Choice):# Choices of this class belong to questionPartOne class and are linked to a specific Holland personality type
    choiceHarmonType=models.ForeignKey(HarmonType)
    question=models.ForeignKey(QuestionPartOne)

class ChoicePartTwo(Choice):# Choices of this class belong to questionPartTwo class and are linked to a specific Study area
    studyA= models.ForeignKey(StudyArea)
    question=models.ForeignKey(QuestionPartTwo)
