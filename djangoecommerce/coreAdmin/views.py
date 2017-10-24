# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
# Create your views here.

class IndexView(TemplateView):
	template_name= 'index.html'

index = IndexView.as_view()

def login(request):
	return render(request, 'login.html')


def plain(request):
	return render(request, 'plain_page.html')




	
