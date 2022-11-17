from django.contrib import admin
from webapp.models import Task, Status, Type
# Register your models here.

class TYPE_STATUS_ADMIN(admin.ModelAdmin):
    list_display = ['name']
class TASK_ADMIN(admin.ModelAdmin):
    list_display = ['summary']

admin.site.register(Task, TASK_ADMIN)
admin.site.register(Status, TYPE_STATUS_ADMIN)
admin.site.register(Type, TYPE_STATUS_ADMIN)