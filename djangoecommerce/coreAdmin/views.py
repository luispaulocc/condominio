# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from braces.views import LoginRequiredMixin

# Create your views here.

#from braces.views import PermissionRequiredMixin



def login(request):
	return render(request, 'login.html')


def page_403(request):
	return render(request, 'page_403.html')


class PlainView(LoginRequiredMixin, TemplateView):
    template_name = 'plain_page.html'
#    permission_required = 'global_permissions.acessar_index'
#    permission_denied_message ='erro'
plain = PlainView.as_view()



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
#    permission_required = 'global_permissions.acessar_index'
#    permission_denied_message ='erro'
index = IndexView.as_view()
