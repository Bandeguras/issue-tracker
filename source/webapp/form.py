from django import forms
from webapp.models import Type, Status
from django.forms import widgets


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=30, label="Summary", required=True)
    description = forms.CharField(max_length=3000, label="Description", required=False,
                                  widget=widgets.Textarea(attrs={"cols": 20, "rows": 3}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Status", required=True)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Type", required=True)
