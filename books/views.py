from django.http import JsonResponse
from .models import Book

# Create your views here.


def getbooks(request):
    books = Book.objects.all()
    return JsonResponse({"books": list(books.values())})
