from django import forms
from webapp.models import Task
from django.forms import widgets


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {'type': widgets.CheckboxSelectMultiple}