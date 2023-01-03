from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        if (cleaned_data['first_name'] or cleaned_data['last_name']) == '':
            raise ValidationError('At least one of the fields (firstname, lastname) must be filled in.')
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise ValidationError('Email is required')
        return email
