from django.db import models
from authors.models import Author

# Create your models here.


class Category(models.Model):
    """
    Category model \n
    |- id (PK) -|- name -|- description -|-category_image-|- created_at -|- updated_at -|

    """

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to="category_images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    """
    Book model \n
    |- id (PK) -|- title -|- description -|- published_date -|- author -|- category -|- cover_image -|- created_at -|- updated_at -|

    """

    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name="authors")
    published_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def likes_count(self):
        return self.likes.all().count()


class Like(models.Model):
    """
    Like model \n
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="book_likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book}'s - {self.user}"


class Comment(models.Model):
    """
    Comment model \n
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="book_comments"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book}'s - {self.comment}"
