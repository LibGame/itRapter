from django import forms

from .models import DjangoComment


class DjangoForm(forms.ModelForm):

    class Meta:
        model = DjangoComment
        fields = ('nameDjango', 'textCommentDjango')