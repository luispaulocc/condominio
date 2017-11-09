"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from coreAdmin.views import index
from coreAdmin.views import plain
from moradores.views import moradores, add_morador
from moradores.views import cadastrar_morador
from django.contrib.auth.views import login, logout_then_login

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    url(r'^inicio/$', index, name='index'),
    url(r'^$', LoginView.as_view(template_name='login.html'), name="login"),    
    url(r'^logout/$',logout_then_login, name="logout"),
    url(r'^plain_page/$', plain, name='plain'),
    url(r'^cadastar_morador$', add_morador, name='cadastrar_morador'),
    url(r'^moradores/$', moradores, name='moradores'),
    url(r'^admin/', admin.site.urls),

]
