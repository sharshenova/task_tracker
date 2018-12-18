from django import forms
from webapp.models import Project

class ProjectSearchForm(forms.Form):
    project_name = forms.CharField(max_length=200, required=False, label='Имя проекта')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # exclude = ['project', 'description'] не включать
        fields = ['project', 'description']