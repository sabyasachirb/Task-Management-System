from django.contrib.auth.models import User
from django import forms

class ProfileUpdateForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']