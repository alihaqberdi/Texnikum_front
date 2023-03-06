from django import forms
from django.contrib.auth.models import User
from .models import Patsient


class PatsientForm(forms.ModelForm):
    class Meta:
        model = Patsient
        fields = ['email',
                  'name',
                  'mobile',
                  'password',
                  'city',
                  'street']
        widgets = {'password': forms.PasswordInput()}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username', 'first_name', 'password'
        widgets = {
            'password': forms.PasswordInput(),
        }