from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import User
from serializers import UserSerializer
from rest_framework import filters

# Create your views here.
class UserList(ListAPIView):
    """
    List all users.
    """

    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["username", "email"]
