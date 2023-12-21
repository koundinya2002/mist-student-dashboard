from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    options = [('Teacher', 'Teacher'),('Teacher', 'Student')]
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control', 'placeholder': 'email',}))
    first_name = forms.CharField(max_length = 255, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 255, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(max_length = 255, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    role = forms.ChoiceField(choices=options)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class login_form(forms.Form):
    username = forms.CharField(max_length=99)
    password = forms.CharField(widget= forms.PasswordInput())