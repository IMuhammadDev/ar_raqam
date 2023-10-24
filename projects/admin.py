from django.contrib import admin

from django.contrib import admin
from .models import Project, Task, Comment, MediaFile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "start_date", "end_date", "manager")
    search_fields = ("name", "description", "manager__username")
    list_filter = ("status", "start_date", "end_date")
    raw_id_fields = ("manager", "developers")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "project", "assigned_to", "due_date")
    search_fields = ("title", "description", "project__name", "assigned_to__username")
    list_filter = ("status", "due_date")
    raw_id_fields = ("project", "assigned_to")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_at", "task", "project")
    search_fields = ("user__username", "content", "task__title", "project__name")
    list_filter = ("created_at",)
    raw_id_fields = ("user", "task", "project")


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_at", "task", "project")
    search_fields = ("task__title", "project__name")
    list_filter = ("uploaded_at",)
    raw_id_fields = ("task", "project")
