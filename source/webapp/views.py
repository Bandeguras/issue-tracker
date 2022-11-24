from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task
from django.views.generic import TemplateView, FormView
from webapp.form import TaskForm


# Create your views here.


class IndexViews(TemplateView):
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


class TaskCreate(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        self.task = Task.objects.create(**form.cleaned_data)
        self.task.type.set(types)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.task.pk})


class TaskUpdate(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status':
            initial[key] = getattr(self.task, key)
        initial['type'] = self.task.type.all()
        return initial

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        self.task.type.set(types)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


class TaskDelete(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')