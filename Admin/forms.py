from django import forms
from .models import Administrator


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        db_table = 'Administrator'
