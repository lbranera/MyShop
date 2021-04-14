from django.forms import ModelForm, TextInput, PasswordInput
from products.models import * 

class UserForm(ModelForm):
    class Meta: 
        model = User
        fields = "__all__"
        widgets = { 
            'first_name': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'name@example.com' , 'required': True, } ),
            'last_name': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'name@example.com' , 'required': True, } ),
            'username': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'name@example.com' , 'required': True, } ),
            'email': TextInput( attrs={ 'type':'email', 'class': 'form-control', 'id':'floatingInput', 'placeholder':'name@example.com' , 'required': True, } ),
            'password': PasswordInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'name@example.com' , 'required': True, } )
        }