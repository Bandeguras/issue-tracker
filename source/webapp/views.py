from django.shortcuts import render, get_object_or_404
from webapp.models import Task
from django.views import View
from django.views.generic import TemplateView
# Create your views here.


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
        }
        return render(request, 'index.html', context)

class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context