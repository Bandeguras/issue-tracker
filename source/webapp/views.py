from django.shortcuts import render
from webapp.models import Task
from django.views import View
# Create your views here.


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
        }
        return render(request, 'index.html', context)