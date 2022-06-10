from django import forms
from .models import BookType


class AddBookType(forms.ModelForm):
    addType = forms.CharField()

    class Meta:
        model = BookType
        fields = ('book_type_name',)


class RemoveBookType(forms.ModelForm):
    delType = forms.CharField()

    class Meta:
        model = BookType
        fields = ('book_type_name',)
