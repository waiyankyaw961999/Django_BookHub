from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BookList.as_view(), name="books"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book"),
]

# Crud: Create, Read, Update, Delete
# /books/
# /books/<int:pk>/
# /books/<int:pk>/edit/
# /books/<int:pk>/delete/
# /books/add/
# /books/<int:pk>/reviews/
# /books/<int:pk>/reviews/add/
# /books/<int:pk>/reviews/<int:pk>/edit/
# /books/<int:pk>/reviews/<int:pk>/delete/
# Likes
# /books/<int:pk>/reviews/<int:pk>/upvote/
# /books/<int:pk>/reviews/<int:pk>/downvote/
# /books/<int:pk>/reviews/<int:pk>/flag/
# /books/<int:pk>/reviews/<int:pk>/unflag/
# /books/<int:pk>/reviews/<int:pk>/report/
# /books/<int:pk>/reviews/<int:id>/unreport/
