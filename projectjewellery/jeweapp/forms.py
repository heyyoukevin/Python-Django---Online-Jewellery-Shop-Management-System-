from django import forms
from django.forms import CharField
from jeweapp.models import pmodel

# ----------------------------------------------user registration-------------------------------------------------------------------------------------------------------------------			 
class pform(forms.Form):
	iname = forms.CharField(max_length=50)
	p_image = forms.FileField()
	class Meta:
		model = pmodel
		fields = ['iname','cname','scame','modal','wght','stonedtl','swght','sprice','mcharge','size','descp','p_image','qty']
		
# ------------------------