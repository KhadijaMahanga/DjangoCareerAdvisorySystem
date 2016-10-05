# this document contains the urls needed for the quiz sub application
# 15 Septermber 2014
# Career Study Advisor

from django.conf.urls import patterns, url
from careerquiz import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='quiz'),
    	url('quizSecond/', views.quizSecond, name='quizSecond'),
    	url('results/', views.results, name='results'),
	url('quizError/', views.quizError, name='quizError'),
	

)
