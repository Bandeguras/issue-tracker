from webapp.models import Project
from django.views.generic import ListView


class ProjectView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
