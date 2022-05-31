from django.db import models
from authors.models import Author

# Create your models here.


class Category(models.Model):
    """
    Category model \n
    |- id (PK) -|- name -|- description -|- created_at -|- updated_at -|

    """

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Category object: {self.name}>"


class Book(models.Model):
    """
    Book model \n
    |- id (PK) -|- name -|- description -|- created_at -|- updated_at -|

    """

    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    published_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Book object: {self.title}>"
