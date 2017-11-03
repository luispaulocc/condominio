# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Apartamento(models.Model):

	name = models.CharField(max_length=100)
	condominio = models.ForeignKey('moradores.Condominio', verbose_name='Condominio')

	class Meta:
		verbose_name = 'Apartamento'
		verbose_name_plural = 'Apartamentos'
		ordering = ['name']	

	def __str__(self):
		return self.name


class Condominio(models.Model):
	name = models.CharField('Condominio', max_length=100)


	class Meta:
		verbose_name = 'Condominio'
		verbose_name_plural = 'Condominios'
		ordering = ['name']	

	def __str__(self):
		return self.name



class Pessoa(models.Model):

	name = models.CharField('Nome', max_length=100)
	sobrenome = models.CharField('sobrenome', max_length=100)
	apartamento = models.ForeignKey('moradores.Apartamento', max_length=20)
	condominio = models.ForeignKey('moradores.Condominio', verbose_name='Condominio')
	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Pessoa'
		verbose_name_plural = 'Pessoas'
		ordering = ['name']

	def __str__(self):
		return self.name
