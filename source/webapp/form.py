from django import forms
from webapp.models import Task, Project
from django.forms import widgets, ValidationError


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Search")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['summary', 'description', 'created_at', 'expiration_at']
        widgets = {'created_at': widgets.SelectDateWidget, 'expiration_at': widgets.SelectDateWidget}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {'type': widgets.CheckboxSelectMultiple}

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 5:
            self.add_error('summary',
                           ValidationError("the length of this field must be at least %(length)d characters!",
                                           code="too_short",
                                           params={'length': 5}))
        if not summary[0].isupper():
            self.add_error('summary',
                           ValidationError("this field must start with a capital letter", code='capital_letter'))
        return summary

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            self.add_error('description',
                           ValidationError("the length of this field must be at least %(length)d characters!",
                                           code="too_short",
                                           params={'length': 10}))
        if 'Lorem ipsum' in description:
            self.add_error('description', ValidationError("you can't use lorem ipsum generator", code="lorem"))
        return description

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError('the title should not duplicate the description')
        return cleaned_data