from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from .form import MyUserCreationForm, UserChangeForm, ProfileChangeForm
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
            next_url = reverse('webapp:project:index')
        return next_url


class UserChangeProjectView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'user_add.html'
    form_class = ChangeUserProjectForm
    permission_required = 'webapp.add_user_in_project'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().author.all()


class UserView(LoginRequiredMixin, DetailView,  MultipleObjectMixin):
    template_name = 'user_view.html'
    model = get_user_model()
    context_object_name = 'user_obj'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        projects = self.get_object().projects.all()
        return super().get_context_data(object_list=projects, **kwargs)


class UserList(PermissionRequiredMixin, ListView):
    template_name = 'user_index.html'
    model = get_user_model()
    context_object_name = 'user_list'
    permission_required = 'accounts.user_list_view'


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'
    form_class_profile = ProfileChangeForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in kwargs:
            context['profile_form'] = self.form_class_profile(instance=self.get_object().profile)
        return context

    def get_success_url(self):
        return reverse('accounts:user_view', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.form_class_profile(instance=self.get_object().profile, data=request.POST, files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_valid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        return self.render_to_response(self.get_context_data(form=form, profile_form=profile_form))


class UserChangePasswordView(PasswordChangeView):
    template_name = 'user_change_password.html'

    def get_success_url(self):
        return reverse('accounts:user_view', kwargs={'pk': self.request.user.pk})

