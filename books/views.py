from rest_framework.response import Response
from yaml import serialize

from authors.serializers import AuthorSerializer
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from authors.serializers import AuthorSerializer

# Create your views here.


class BookList(ListAPIView):
    """
    List all books, or create a new book.
    """

    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
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
