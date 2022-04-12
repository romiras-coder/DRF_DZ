from django.contrib import admin
from .models.project import Project
from .models.todo import Todo


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_create',)
    search_fields = ('pk', 'name',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_create',)
    search_fields = ('pk',)
