from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.db.models import Q


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        if Q(cleaned_data['first_name']) | Q(cleaned_data['last_name']) is "":
            raise ValidationError('At least one of the fields (firstname, lastname) must be filled in.')
        return cleaned_data