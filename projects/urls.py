from django.urls import path
from .views import (
    ProjectList,
    ProjectDetail,
    TaskList,
    TaskDetail,
    CommentList,
    CommentDetail,
    MediaFileList,
    MediaFileDetail,
)

urlpatterns = [
    path("projects/", ProjectList.as_view(), name="project-list"),
    path("projects/<int:pk>/", ProjectDetail.as_view(), name="project-detail"),
    path("tasks/", TaskList.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("comments/", CommentList.as_view(), name="comment-list"),
    path("comments/<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
    path("media-files/", MediaFileList.as_view(), name="mediafile-list"),
    path("media-files/<int:pk>/", MediaFileDetail.as_view(), name="mediafile-detail"),
]
