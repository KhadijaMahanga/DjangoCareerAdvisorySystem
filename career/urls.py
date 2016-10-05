# this documents contains the urls needed for the core browsing and profile management features of the application
# 15 September 2014
# Career Study Advisor

from django.conf.urls import patterns, url
from career import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('login/', views.user_login, name='login'),
    url('contact/', views.contact, name='contact'),
    url('studyareas/', views.studyareas, name='studyareas'),
    url('institutions/', views.institutions, name='institutions'),
    url('programmes/', views.programmes, name='programmes'),
    url('faq/', views.faq, name='faq'),
    url('quiz/', views.quiz, name='quiz'),
    url('about/', views.about, name='about'),
    url('sitemap/', views.sitemap, name='sitemap'),
    url('register/', views.register, name='register'),
    url('logout/', views.user_logout, name='logout'),
    url('searchresult/', views.searchresult, name='searchresult'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^student/(?P<user_pk>\d+)$', views.student, name='student'),
    url('loginerror/', views.loginerror, name='loginerror'),
    url('reminderset/', views.reminderset, name='reminderset'),
)
