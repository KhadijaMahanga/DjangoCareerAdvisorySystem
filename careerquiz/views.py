# This document contains the views needed for the quiz sub application
# 15 September 2014	
# Career study advisor

from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from careerquiz.models import Question, Choice,Quiz,QuestionPartOne,ChoicePartOne,QuestionPartTwo,ChoicePartTwo,HarmonType
from career.models import StudyArea
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout


def index(request):
    quiz= Quiz()
    if request.method == 'POST' and 'next' in request.POST:# if the user is in the first half of the quiz
	# list of question selections
	answerList=[] 
	#Check if all questions in the quiz were answered. If not, inform the user to go back
	try:
	    for i in range(QuestionPartOne.objects.all().count()):
	    	answerList.append(request.POST[str(i+1)])# gets the answer for each question and add to the list of questions
	except:
	    template=loader.get_template('careerquiz/quizError.html')
    	    context=RequestContext(request)
   	    return HttpResponse(template.render(context))
	
	quiz.calculateQuizResultPartOne( answerList )# calculate the personality type
	template=loader.get_template('careerquiz/quizSecond.html')
	latest_question_list = QuestionPartTwo.objects.filter(harmonTypeText=quiz.result)
	# filters though questions for the specific Harmon category questions
    	context = RequestContext(request,{'latest_question_list': latest_question_list,},)
        resultPartOne=quiz.result
	return HttpResponse(template.render(context))
	
    elif request.method=='POST'and 'getresult' in request.POST:# if the user is in the second half of the quiz
	#Check if all questions in the quiz were answered. If not, inform the user to go back
	try:
	    partTwoChoice="default"
	    hollandType="default"
	    try:#get the specific study areas based on the choice selected.
	        hollandType='Realistic'
	        partTwoChoice=request.POST['Realistic']
            except:
	        try:
		    hollandType='Social'	
	    	    partTwoChoice=request.POST['Social']
		except:
		    try:
		        hollandType='Artistic'	
	    	        partTwoChoice=request.POST['Artistic']
	    	    except:
		        try:
			    hollandType='Conventional'
 		    	    partTwoChoice=request.POST['Conventional']
		        except:
			    try:
			        hollandType='Enterprising'
			        partTwoChoice=reques.POST['Enterprising']
			    except:
			        hollandType='Investigative'
			        partTwoChoice.POST['Investigative']
	    holland_type_list=HarmonType.objects.get(name=hollandType) # gets the specific personality type
	    studyarea_list=StudyArea.objects.get(title=partTwoChoice) # gets the study areas
	    template=loader.get_template('careerquiz/results.html')
	    context = RequestContext(request, {'studyarea_list': studyarea_list,'holland_type_list': holland_type_list,},)
    	    return HttpResponse(template.render(context))	
	except:
	    template=loader.get_template('careerquiz/quizError.html')
    	    context=RequestContext(request)
   	    return HttpResponse(template.render(context))
    else:
	latest_question_list = QuestionPartOne.objects.all() # list all questions in the first part of the quiz
    	template=loader.get_template('careerquiz/quiz.html')
    	context = RequestContext(request, {'latest_question_list': latest_question_list,},)
    	return HttpResponse(template.render(context))

def results(request, result):# load the results page
    template=loader.get_template('careerquiz/results.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

def quizSecond(request):
    return HttpResponse("")

def quizError(request):# load the error page if all questions were not answered
    template=loader.get_template('careerquiz/quizError.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))
