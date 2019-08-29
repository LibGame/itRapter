from django import forms
from django.forms import ModelForm


class SearchFormProgramm(forms.Form):
    queryProgramm = forms.CharField()

