from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 
from products.models import * 

'''
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
'''

class UserForm(UserCreationForm):
    attrs = { 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Password' , 'required': True, } 
    password1 =  CharField( widget=PasswordInput(attrs=attrs) )
    password2 =  CharField( widget=PasswordInput(attrs=attrs) )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = { 
            'first_name': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter First Name', 'required': True, } ),
            'last_name': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Last Name', 'required': True, } ),
            'username': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput' , 'placeholder':'Enter Username', 'required': True, } ),
            'email': TextInput( attrs={ 'type':'email', 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Email Address', 'required': True, } ),
        }

class ShoppingCartForm(ModelForm):
    class Meta:
        model = ShoppingCart
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'book':  HiddenInput( attrs = {'type':'hidden'} ),
            'quantity': NumberInput ( attrs = {'class':'form-control', 'min':'1'} ),
        }