from django import forms
from django.forms import ModelForm
from .models import CommentModel


class SearchForm(forms.Form):
    query = forms.CharField()
    


class Comments(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ('name', 'text')