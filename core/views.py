from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @login_required
# def user_role_view(request):
#     if request.user.role == "developer":
#         # Developer specific logic
#         pass
#     elif request.user.role == "manager":
#         # Manager specific logic
#         pass
#     elif request.user.role == "client":
#         # Client specific logic
#         pass


# def is_developer(user):
#     return user.groups.filter(name="Developer").exists()


# @login_required
# @user_passes_test(is_developer)
# def developer_view(request):
#     pass
