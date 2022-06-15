from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BookList.as_view(), name="book-list"),
    # Filter books by id, name, isbn, category, author.
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book-detail"),
    # path("books/<int:pk>/authors/", views.ReviewList.as_view(), name="books-authors"),
    # path("books/<int:pk>/reviews/", views.ReviewList.as_view(), name="books-reviews"),
]

# Crud: Create, Read, Update, Delete

# /books/<int:pk>/reviews/

# Likes
# /books/<int:pk>/reviews/
# /books/<int:pk>/reviews/
# /books/<int:pk>/reviews/<int:pk>/report
# /books/<int:pk>/reviews/<int:pk>/like/
