from django import forms

from .models import JarComment


class JarForm(forms.ModelForm):

    class Meta:
        model = JarComment
        fields = ('nameJar', 'textCommentJar')