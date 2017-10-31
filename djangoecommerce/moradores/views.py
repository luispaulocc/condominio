# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from django.shortcuts import render

from .models import Condominio, Pessoa, Morador

# Create your views here.



class CadastroMoradoresListView(generic.ListView):

	model = Morador
	template_name = 'cadastrar_morador.html'
	context_object_name = 'cadastrar_morador'


cadastrar_morador = CadastroMoradoresListView.as_view()


class MoradoresListView(generic.ListView):

	model = Morador
	template_name = 'moradores.html'
	context_object_name = 'moradores'


moradores = MoradoresListView.as_view()