from django import forms
from webapp.models import Task
from django.forms import widgets


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Search")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {'type': widgets.CheckboxSelectMultiple}