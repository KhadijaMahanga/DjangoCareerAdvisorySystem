# this document contains the views needed for the core browsing and profile management pages
# 15 September 2014
# Career Study Advisor

from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from career.models import Institution, StudyArea, Programme, UserProfile,Reminder
from career.forms import UserForm, UserProfileForm, AdvisorProfileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('career/institutions/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login.html', {'form': form})

def index(request):
    template=loader.get_template('career/index.html')
    context=RequestContext(request)
    #return HttpResponse("Hello, world. You're at the poll index.")
    return HttpResponse(template.render(context))

#def chat_room(request, chat_room_id):
   # chat = get_object_or_404(ChatRoom, pk=chat_room_id)
   # return render(request, 'career/chat_room.html', {'chat': chat})

def contact(request):
    template=loader.get_template('career/contact.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

def studyareas(request):
    template=loader.get_template('career/studyareas.html')
    studyAreaList=StudyArea.objects.all()
    context=RequestContext(request,{'studyAreaList':studyAreaList,})	
    return HttpResponse(template.render(context))


def institutions(request):
    template=loader.get_template('career/institutions.html')
    institutionList= Institution.objects.all()
    context=RequestContext(request,{'institutionList':institutionList,})
    return HttpResponse(template.render(context))


def programmes(request):
    if request.method == 'POST': # if the user wants to add a reminder to his profile
	date=request.POST["date"]
	user=User.objects.get(username=request.user)# Users name 
	#Create a new reminder object
	reminderObject=Reminder(user,date)
	reminderObject.set_username=user
	reminderObject.set_dateCourse=date

	template=loader.get_template('career/reminderset.html')
    	context=RequestContext(request)
    	return HttpResponse(template.render(context))
    
    template=loader.get_template('career/programmes.html')
    institutionList= Institution.objects.all()
    studyAreaList=StudyArea.objects.all()
    programmeList=Programme.objects.all()
    context=RequestContext(request,{'institutionList':institutionList,'studyAreaList':studyAreaList,'programmeList':programmeList,})
    return HttpResponse(template.render(context))


def about(request):
    template=loader.get_template('career/about.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

def faq(request):
    template=loader.get_template('career/faq.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

def sitemap(request):
    template=loader.get_template('career/sitemap.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

def quiz(request):
    template=loader.get_template('career/quiz.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))


def register(request):
    registered = False

   
    if request.method == 'POST':
	
	user_form = UserForm(data=request.POST)
	profile_form = UserProfileForm(data=request.POST)

	if user_form.is_valid() and profile_form.is_valid():
	    user = user_form.save()
	    user.set_password(user.password)
	    user.save()
	    profile = profile_form.save(commit=False)
	    profile.user = user
	    profile.save()
	    registered = True

	else:
	    print user_form.errors, profile_form.errors


    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
	user_form = UserForm()
	profile_form = UserProfileForm()
		

    template=loader.get_template('career/register.html')
    context = RequestContext(request,{'user_form':user_form, 'student_form':profile_form, 'registered':registered,})
    return HttpResponse(template.render(context))




def user_login(request):

    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
	if user:
       	    if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/career/')
            else:
                return HttpResponse("Your account is disabled.")
        else:

            template=loader.get_template('career/loginerror.html')
    	    context=RequestContext(request)
    	    return HttpResponse(template.render(context))

    else:
      
        template=loader.get_template('career/login.html')
    	context=RequestContext(request)
    	return HttpResponse(template.render(context))

def loginerror(request):# load the error page if login incorrect
    template=loader.get_template('career/loginerror.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/career/')

def searchresult(request):
    
    searchvalue = request.POST['searchvalue']

    stdy = StudyArea.objects.filter(description__contains=searchvalue)
    prog = Programme.objects.filter(description__contains=searchvalue)

    searchresult={}
    searchresult['studyAreaList']=stdy
    searchresult['programmeList']= prog
    
    template=loader.get_template('career/searchresult.html')
    context = RequestContext(request, searchresult)
    return HttpResponse(template.render(context))


def profile(request):

    context = RequestContext(request)
    u = User.objects.get(username=request.user)
    up = u.get_profile()
  
    context_dict={}
    context_dict['user'] = u
    context_dict['studentuser'] = up
    return render_to_response('career/profile.html', context_dict, context)

def student(request, user_pk):
    u = User.objects.get(username=request.user)
    studentpf = u.get_profile()

    if request.method == "POST":
        pf = UserProfileForm(data=request.POST, instance=studentpf)
        if pf.is_valid():
            pf.save()
	    template=loader.get_template('career/profile.html')
    	    context=RequestContext(request)
    	    return HttpResponse(template.render(context))
	else:
	    pf = UserProfileForm(instance=studentpf)
 	    sty = 'Invalid inputs'
    	    template=loader.get_template('career/student.html')
    	    context = RequestContext(request,{'user_form':pf, 'error': sty})
    	    return HttpResponse(template.render(context))  
		
    else:
	pf = UserProfileForm(instance=studentpf)
    	template=loader.get_template('career/student.html')
    	context = RequestContext(request,{'user_form':pf,})
    	return HttpResponse(template.render(context))


def reminderset(request):# inform user that reminder was set
    template=loader.get_template('career/reminderset.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))

