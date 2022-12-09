from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task, Project
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.form import TaskForm, SearchForm


# Create your views here.


class TaskIndex(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class TaskView(DetailView):
    template_name = 'task/task_view.html'
    model = Task


class TaskCreate(CreateView):
    template_name = 'task/task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm
    context_object_name = "projects"

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.project.pk})


class TaskDelete(DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.project.pk})
