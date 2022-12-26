from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from accounts.form import MyUserCreationForm
from .models import Profile
from webapp.models import Project


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url


class UserAdd(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'user_add.html'
    fields = ['author']
    permission_required = 'auth.add_user'

    def has_permission(self):
        if self.request.user in self.get_object().author.all():
            return self.request.user.has_perm('auth.add_user')


class UserDelete(PermissionRequiredMixin, DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('webapp:project_index')
    permission_required = 'auth.delete_user'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class UserView(DetailView):
    template_name = 'user_view.html'
    model = get_user_model()
    context_object_name = 'user_obj'
