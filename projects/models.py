from django.db import models
from django.conf import settings


# Create your models here.

PROJECT_STATUS_CHOICES = (
    ("not_started", "Not Started"),
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
    ("on_hold", "On Hold"),
)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=PROJECT_STATUS_CHOICES, default="not_started"
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="managed_projects",
        null=True,
        blank=True,
    )
    developers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="projects"
    )

    def __str__(self):
        return self.name


TASK_STATUS_CHOICES = (
    ("not_started", "Not Started"),
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
    ("blocked", "Blocked"),
)


class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=50, choices=TASK_STATUS_CHOICES, default="not_started"
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey("Task", on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Comment by {self.user} on {self.created_at}"


class MediaFile(models.Model):
    file = models.FileField(upload_to="media/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True
    )
