"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import TaskIndex, TaskView, TaskCreate, TaskUpdate, TaskDelete, ProjectIndex, ProjectView, ProjectCreate, ProjectUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectIndex.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='project_update'),

    path('task/<int:pk>/', TaskView.as_view(), name='task'),
    path('task/index/', TaskIndex.as_view(), name='task_index'),
    path('project/<int:pk>/create/task/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='delete'),

]
