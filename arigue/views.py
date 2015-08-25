from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, FileResponse
from django.template import loader
from django.contrib import auth


# Create your views here.

# index view 
def index(request):
 	t = loader.get_template('index.html')	
	return HttpResponse(t.render())

# arigue view
def arigue(request):
	return render_to_response('index.html', {})


# login view
def login(request):
	# print request.POST
	# print request.POST.get('username')
	# print request.POST.get('password')

	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username, password=password)
  	
  	if user is not None:
		auth.login(request, user)
  		return HttpResponseRedirect('/dashboard')
  	else:
		return render_to_response('index.html', {'login err': 'Wrong username or password'})		


# logout view
def logout(request):
	logout(request)


# Dashboard view
def dashboard(request):
	return render_to_response('dashboard.html', {'user': request.user})
