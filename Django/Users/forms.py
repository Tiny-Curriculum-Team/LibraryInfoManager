from django import forms
from django.contrib.auth.models import User
from .models import Reader


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        db_table = 'Reader'


class UserRegisterForm(forms.ModelForm):
    reader_name = forms.CharField()
    user_name = forms.CharField()
    tel = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = Reader
        fields = ('reader_name', 'user_name', 'tel')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password1') == data.get('password2'):
            return data.get('password1')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")
