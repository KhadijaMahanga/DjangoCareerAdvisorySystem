from django.http import*
from datetime import datetime
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
import socket, select, string, sys
import json



def index(request):
    template=loader.get_template('careerchat/basechat.html')
    context=RequestContext(request)
    return HttpResponse(template.render(context))



def testajax(request):
    if request.method == "POST":
	x = request.POST['client_response']
	z= request.POST['user_name']
	timenow = datetime.datetime.now()
	y = timenow.strftime("%H:%M:%S")
	response_data={}
	response_data.update({'response': x})

	return HttpResponse("Hello, world. You're at the poll index.")
	#return HttpResponse(json.dumps(response_data), mimetype='application/json')
    else:
	return HttpResponse("Hello, world. You're at the poll index.")
    #return render_to_response('basechat.html', response_data)
    
