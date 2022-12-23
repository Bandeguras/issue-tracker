from django.contrib.auth import login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from accounts.form import MyUserCreationForm
from webapp.form import ProjectForm
from webapp.models import Project


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
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
