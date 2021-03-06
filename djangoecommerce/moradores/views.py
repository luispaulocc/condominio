# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from django.shortcuts import render, redirect

from django.shortcuts import get_list_or_404, get_object_or_404
from django import forms
from django.utils import timezone
from forms import  CadastroMoradorForm
from .models import Condominio, Pessoa, Apartamento
from braces.views import LoginRequiredMixin
from braces.views import PermissionRequiredMixin


def add_morador(request):
 
    if request.method == "POST":
        form = CadastroMoradorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/inicio')
 
    else:
 
        form = CadastroMoradorForm()
        return render(request, "cadastrar_morador.html", {'form': form})



class CadastroMoradoresListView(LoginRequiredMixin, generic.ListView):
    model = Pessoa
    template_name = 'cadastrar_morador.html'
    context_object_name = 'cadastrar_morador'

cadastrar_morador = CadastroMoradoresListView.as_view()


class MoradoresListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Pessoa
    template_name = 'moradores.html'
    context_object_name = 'moradores'
    permission_required = 'global_permissions.acessar_index'
    permission_denied_message = 'Permission Denied'
    raise_exception = True
    


moradores = MoradoresListView.as_view()



def morador_edit(request, pk):
    morador = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        form = CadastroMoradorForm(request.POST, instance=morador)
        if form.is_valid():
            morador = form.save(commit=False)
            morador.timestamp = timezone.now()
            morador.save()
            return redirect('moradores')
    else:
        form = CadastroMoradorForm(instance=morador)
    return render(request, 'editar_morador.html', {'form': form})


