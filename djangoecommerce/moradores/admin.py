# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Pessoa, Morador

admin.site.register(Pessoa)
admin.site.register(Morador)