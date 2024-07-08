from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=256 , min_length=11)
    password = forms.CharField(min_length=8)
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(min_length=8)