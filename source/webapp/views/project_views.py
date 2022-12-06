from webapp.models import Project
from webapp.form import ProjectForm
from django.views.generic import ListView, DetailView, CreateView


class ProjectIndex(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project




class ProjectCreate(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm
