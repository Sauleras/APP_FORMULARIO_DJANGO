from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from core.models import *

class RegisterForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']