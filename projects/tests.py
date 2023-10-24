from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Task, Comment, MediaFile


class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.project = Project.objects.create(
            name="Test Project", description="A test project", manager=self.user
        )

    def test_project_creation(self):
        self.assertIsInstance(self.project, Project)
        self.assertEqual(str(self.project), "Test Project")


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.project = Project.objects.create(
            name="Test Project", description="A test project", manager=self.user
        )
        self.task = Task.objects.create(
            title="Test Task", description="A test task", project=self.project
        )

    def test_task_creation(self):
        self.assertIsInstance(self.task, Task)
        self.assertEqual(str(self.task), "Test Task")


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.comment = Comment.objects.create(user=self.user, content="A test comment")

    def test_comment_creation(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertTrue("A test comment" in str(self.comment))


class MediaFileModelTest(TestCase):
    def setUp(self):
        pass

    def test_media_file_creation(self):
        pass
