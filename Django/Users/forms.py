from django import forms
from .models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        db_table = 'User'


class UserRegisterForm(forms.ModelForm):
    nickname = forms.CharField()
    name = forms.CharField()
    tel = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('nickname', 'name', 'tel')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password1') == data.get('password2'):
            return data.get('password1')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")
