from django.contrib import admin
from .models import Book, Category, Like, Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
