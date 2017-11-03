from django.forms import ModelForm
from models import  Pessoa
 


class CadastroMoradorForm(ModelForm):
	class Meta:
		model = Pessoa
		fields = ['name','sobrenome','apartamento','condominio']


