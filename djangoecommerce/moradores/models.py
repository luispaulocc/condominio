# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pessoa(models.Model):


	name = models.CharField('Nome', max_length=100)
	sobremone = models.CharField('sobrenome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Pessoa'
		verbose_name_plural = 'Pessoas'
		ordering = ['name']


	def __str__(self):
		return self.name

class Morador(models.Model):
	apartamento = models.CharField('Apartamento', max_length=20)
	pessoa = models.ForeignKey('moradores.Pessoa', verbose_name='Pessoa')
	slug = models.SlugField('Identificador', max_length=100)


	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Morador'
		verbose_name_plural = 'Moradores'
		ordering = ['apartamento']

	def __str__(self):
		return self.apartamento