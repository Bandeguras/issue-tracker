from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from webapp.models import Project
from webapp.form import ProjectForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectIndex(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = "projects"


class ProjectDelete(LoginRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = "project"
    success_url = reverse_lazy('webapp:project_index')
