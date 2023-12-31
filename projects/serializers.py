from rest_framework import serializers
from .models import Project, Task, Comment, MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    media_files = MediaFileSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    media_files = MediaFileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
