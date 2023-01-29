from django.urls import path
from webapp.views import TaskIndex, TaskView, TaskCreate, TaskUpdate, TaskDelete, ProjectIndex, ProjectView, ProjectCreate, ProjectUpdate,  ProjectDelete, ProjectsLikes

app_name = 'webapp'

urlpatterns = [
    path('', ProjectIndex.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='project_delete'),

    path('task/index/', TaskIndex.as_view(), name='task_index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task'),
    path('project/<int:pk>/create/task/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('project/like/<int:pk>', ProjectsLikes.as_view(), name='project_like'),

]
