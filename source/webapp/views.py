from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from django.views import View
from django.views.generic import TemplateView, RedirectView
from webapp.form import TaskForm


# Create your views here.


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        search_task = self.request.GET.get('search')
        print(search_task)
        if search_task:
            tasks = Task.objects.all().filter(summary=search_task)
            context = {'task': tasks}
            return render(request, 'index.html', context)
        context = {'tasks': tasks}
        return render(request, 'index.html', context)


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreate(RedirectView):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm()
            return render(request, "task_create.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']

            )
            return redirect('index')
        else:
            return render(request, "task_create.html", {'form': form})


class TaskUpdate(RedirectView):

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type,
        })
        return render(request, 'task_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.type = form.cleaned_data.get('type')
            task.save()
            return redirect('index')
        else:
            return render(request, 'task_update.html', {'form': form})


class TaskDelete(RedirectView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')