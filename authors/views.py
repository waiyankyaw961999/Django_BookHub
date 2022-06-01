from django.shortcuts import render
from authors.serializers import AuthorSerializer
from .models import Author
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class AuthorList(ListAPIView):
    """
    List all authors, or create a new book.
    """

    queryset = Author.objects.all().order_by("-created_at")
    serializer_class = AuthorSerializer
    # Since the default pagination is set in the settings, you don't need to specify it here.
    # pagination_class = PageNumberPagination


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a author instance.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
