# this document contains the classes needed to add information and specifies what data can be modified by administrative staff
# 15 Spetember 2014
# Career Study Advisor

from django.contrib import admin
from career.models import Programme, Institution, StudyArea,Reminder
from careerquiz.models import QuestionPartOne,ChoicePartOne,HarmonType, ChoicePartTwo,QuestionPartTwo, Choice, Question
from career.models import UserProfile

class ChoiceInLine(admin.TabularInline): 
    model=ChoicePartOne
    extra=5
class ChoiceTwoInLine(admin.TabularInline):
    model=ChoicePartTwo
    extra=5

class QuestionAdmin(admin.ModelAdmin): 
    inlines = [ChoiceInLine]# add choices to the question on the same page

class QuestionTwoAdmin(admin.ModelAdmin):
    inlines=[ChoiceTwoInLine]# add choices to the question on the same page

#modify the various classes shown in brackets
admin.site.register(Programme)
admin.site.register(StudyArea)
admin.site.register(Institution)
admin.site.register(UserProfile)
admin.site.register(QuestionPartOne, QuestionAdmin)
admin.site.register(QuestionPartTwo,QuestionTwoAdmin)
admin.site.register(HarmonType)


