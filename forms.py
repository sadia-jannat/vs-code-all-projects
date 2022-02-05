import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets


#project form create
from .models import Useri, houserate 
from .models import Userform
from .models import Ownerform

from.models import r
from.models import houserate


#django form create kore bellow models and forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms







#Here class create and add new name by me

class StudentReg(forms.ModelForm):
    class Meta:
        model=Useri
        fields=['name','email','password']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
        


class UserReg(forms.ModelForm):
    class Meta:
        model=Userform
        fields=['name','email','password', 'code']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'code':  forms.TextInput(attrs={'class':'form-control'}),
        }
        


class OwnerformReg(forms.ModelForm):
    class Meta:
        model=Ownerform
        fields=['ownername', 'email', 'ownerpin', 'housecategory', 'housename',  'division',
    'district', 'area', 'housesize', 'bedroom', 'dinning', 'drawing', 'bathroom', 'kitchen', 'balcony',
    'housedetail', 'img', 'houserent']

        labels={'ownername':'Your Name', 'email':'Your Email', 'ownerpin':'Your pin', 'housecategory': 'House Category', 
    'housename': 'House Name',  'division': 'Division',
    'district': 'District', 'area':'Area', 'housesize': 'House-Size', 'bedroom':'Bedroom', 'dinning':'Dinning', 
    'drawing': 'Drawing', 'bathroom':'Bathroom', 'kitchen': 'Kitchen', 'balcony':'Balcony',
    'housedetail':'House Details', 'img':'House Image', 'houserent':'House Rent'}
    
        widgets={
            'ownername': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'ownerpin': forms.NumberInput(attrs={'class':'form-control'}),
            'housecategory':  forms.TextInput(attrs={'class':'form-control'}),
            'housename':  forms.TextInput(attrs={'class':'form-control'}),
            'division':  forms.Select(attrs={'class':'form-select'}),
            'district':  forms.TextInput(attrs={'class':'form-control'}),
            'area':  forms.TextInput(attrs={'class':'form-control'}),
            'housesize':  forms.TextInput(attrs={'class':'form-control'}),

            'bedroom': forms.NumberInput(attrs={'class':'form-control'}),
            'dinning': forms.NumberInput(attrs={'class':'form-control'}),
            'drawing': forms.NumberInput(attrs={'class':'form-control'}),
            'bathroom': forms.NumberInput(attrs={'class':'form-control'}),
            'kitchen': forms.NumberInput(attrs={'class':'form-control'}),
            'balcony': forms.NumberInput(attrs={'class':'form-control'}),

            'housedetail':  forms.TextInput(attrs={'class':'form-control'}),
           
            'houserent':  forms.TextInput(attrs={'class':'form-control'}),
        }

           
 
    

#test tes ppage a rate ar jonno
class rreg(forms.ModelForm):
    class Meta:
        model=r
        fields=['main', 'rate', 'reeview']    

        

#houserate model ar form houserateform
class houserateform(forms.ModelForm):
    class Meta:
        model=houserate
        fields=['info_review', 'info_rate']


#here django create his own model and forms..we use their form and model auto create
# class name dilm ami..{SignUp}
class Create(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2' ]



