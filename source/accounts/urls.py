from django.urls import path

from accounts.views import login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

# from django.urls import path
# from accounts.views import login_view, logout_view
#
# app_name = 'accounts'
# urlpatterns = [
#     path('accounts/login', login_view, name='login'),
#     path('accounts/logout', logout_view, name='logout')
#
# ]

