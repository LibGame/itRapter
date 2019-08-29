from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('')

        return email

    def clean_password2(self):
             cd = self.cleaned_data
             if cd['password1'] != cd['password2']:
                 raise forms.ValidationError('Вы ввели раззные пороли')
             return cd['password2']

