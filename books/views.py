from re import purge
from rest_framework.decorators import api_view
from rest_framework import renderers
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
from django.db.models import Q


class BookList(ListAPIView):
    """
    List all books, or create a new book.
    @ https://www.django-rest-framework.org/api-guide/filtering/
    """

    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["category", "title", "isbn", "author"]

    # def get_queryset(self):
    #     name = self.request.query_params.get("name", None)
    #     isbn = self.request.query_params.get("isbn", None)
    #     category = self.request.query_params.get("category", None)
    #     author = self.request.query_params.get("author", None)
    #     if name:
    #         return self.queryset.filter(title__icontains=name)
    #     if isbn:
    #         return self.queryset.filter(isbn=isbn)
    #     if category:
    #         return self.queryset.filter(category=category)

    #     return self.queryset

    # Since the default pagination is set in the settings, you don't need to specify it here.
    # pagination_class = PageNumberPagination


class BookDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a book instance.
    """

    queryset = Book.objects.all()

    serializer_class = BookSerializer
    # def get_object(self, book_id):
    #     try:
    #         return Book.objects.get(pk = book_id)
    #     except Book.DoesNotExist:
    #         raise Http404

    # def get(self,request,book_id,format="json"):
    #     book = self.get_object(book_id)
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data)

    # def put(self,request,book_id,format="json"):
    #     book = self.get_object(book_id)
    #     serializer = BookSerializer(book,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
