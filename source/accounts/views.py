from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from accounts.form import MyUserCreationForm
from webapp.form import ChangeUserProjectForm
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


class UserChangeProjectView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'user_add.html'
    form_class = ChangeUserProjectForm
    permission_required = 'accounts.add_profile'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def has_permission(self):
        if self.request.user in self.get_object().author.all():
            return self.request.user.has_perm('accounts.add_profile')


class UserView(DetailView,  MultipleObjectMixin):
    template_name = 'user_view.html'
    model = get_user_model()
    context_object_name = 'user_obj'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        projects = self.get_object().projects.all()
        return super().get_context_data(object_list=projects, **kwargs)


class UserIndex(PermissionRequiredMixin, ListView):
    template_name = 'user_index.html'
    model = get_user_model()
    context_object_name = 'user_list'
    permission_required = 'accounts.view_profile'


