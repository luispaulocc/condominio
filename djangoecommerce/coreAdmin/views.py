# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.





def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')


def plain(request):
	return render(request, 'plain_page.html')
