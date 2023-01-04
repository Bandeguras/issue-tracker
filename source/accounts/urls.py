from django.urls import path
from accounts.views import RegisterView, UserChangeProjectView, UserView, UserList, UserChangeView, UserChangePasswordView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('project/user_add/<int:pk>/', UserChangeProjectView.as_view(), name='user_add'),
    path('<int:pk>/', UserView.as_view(), name='user_view'),
    path('users/', UserList.as_view(), name='user_index'),
    path('user/update/profile/', UserChangeView.as_view(), name='user_update_profile'),
    path('user/change/password/', UserChangePasswordView.as_view(), name='user_change_password'),

]
