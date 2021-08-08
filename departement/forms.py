from django import forms
from django.forms import fields
from .models import Etudiant

class EleveForm(forms.ModelForm):
    class Meta:
        model =Etudiant
        fields = ['prenom','nom','email','date_de_naissance','lieu_de_naissance']