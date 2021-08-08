from django.forms import ModelForm
from home.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['nom' , 'prenom' ,'email','date','lieu','code','departement','classe']
