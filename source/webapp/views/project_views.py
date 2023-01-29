from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from webapp.models import Project
from webapp.form import ProjectForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse


class ProjectsLikes(View):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))

        data = {
            'like': project.likes.all().count(),
        }

        response = JsonResponse(data)
        print(project.likes.all().count())

        return response



class ProjectIndex(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 5


class ProjectView(LoginRequiredMixin, DetailView):
    template_name = 'project/project_view.html'
    model = Project


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'webapp.add_project'

    def form_valid(self, form):
        form.save()
        form.instance.author.add(self.request.user.pk)
        return super().form_valid(form)


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = "projects"
    permission_required = 'webapp.change_project'


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = "projects"
    permission_required = 'webapp.delete_project'
    success_url = reverse_lazy('webapp:project_index')

