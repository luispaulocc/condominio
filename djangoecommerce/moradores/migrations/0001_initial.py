# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Condominio',
                'verbose_name_plural': 'Condominios',
            },
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.CharField(max_length=20, verbose_name='Apartamento')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Modificado em')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moradores.Condominio', verbose_name='Condominio')),
            ],
            options={
                'ordering': ['apartamento'],
                'verbose_name': 'Morador',
                'verbose_name_plural': 'Moradores',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobremone', models.CharField(max_length=100, verbose_name='sobrenome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Modificado em')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moradores.Condominio', verbose_name='Condominio')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.AddField(
            model_name='morador',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moradores.Pessoa', verbose_name='Pessoa'),
        ),
    ]
