# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	texts =['Lorem ipsum dolor sit amet','consectetur adipisicing elit']
	context = {
		'title': 'django e-commerce',
		'texts': texts
	}

	return render(request, 'index.html', context)

def tables(request):
	return render(request, 'tables.html')

def register(request):
	return render(request, 'register.html')

def forms(request):
	return render(request, 'forms.html')

def login(request):
	return render(request, 'login.html')

def charts(request):
	return render(request, 'charts.html')
