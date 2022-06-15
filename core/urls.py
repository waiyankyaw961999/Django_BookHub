from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from books import views


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "books": reverse("book-list", request=request, format=format),
            "authors": reverse("author-list", request=request, format=format),
            "cateogries": reverse("category-list", request=request, format=format),
        }
    )


urlpatterns = format_suffix_patterns(
    [
        path("", api_root),
        # Admin Dashboard
        path("admin/", admin.site.urls),
        # Categories
        path("categories/", views.CategoryList.as_view(), name="category-list"),
        path(
            "categories/<int:pk>/",
            views.CategoryDetail.as_view(),
            name="category-detail",
        ),
        # Books
        path("", include("books.urls")),
        # Authors
        path("", include("authors.urls")),
    ]
)
