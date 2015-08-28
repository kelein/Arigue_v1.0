from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, FileResponse
from django.template import loader
from django.contrib import auth

from django.core.paginator import Paginator

from arigue.models import *
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

# Server manager view
def server(request):
  	t = loader.get_template('server.html')
	# Get all objects in model Server
	allServers = Server.objects.all()
	# Records of each page
	pageSize = 5
	# Instance a Paginator object 
	paginator = Paginator(allServers, pageSize)	
	# Total page number
	pageCount = paginator.num_pages
	print "Total Page: %s" % pageCount

	# ## Exception Solutino ##	
	try:
  		pageIndex = int(request.GET.get('page', '1'))
		print "Page Index: %s" % pageIndex
	except ValueError:
		pageIndex = 1
		perPage = paginator.page(pageIndex)	
	# Raised when page() is given a valid value but 
	# no objects exist on that page.
	try:
		perPage = paginator.page(pageIndex)	
	except (EmptyPage, InvaildPage):
		perPage = paginator.page(pageCount)	
	
	return render_to_response('server.html', {'perPage': perPage})
