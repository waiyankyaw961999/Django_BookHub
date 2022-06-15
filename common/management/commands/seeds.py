from django.core.management.base import BaseCommand, CommandError
from accounts.models import User
from books.models import Book, Category
from authors.models import Author
from faker import Faker

from .seedingUsers import UserSeeding
from .seedingCategories import CategorySeeding
from .seedingAuthors import AuthorSeeding
from .seedingBooks import BookSeeding


# DEFAULT_NUMBERS
NUMBER_OF_USERS = 50
NUMBER_OF_AUTHORS = 20
NUMBER_OF_BOOKS = 50
NUMBER_OF_CATEGORIES = 6


class Command(BaseCommand):
    help = "Genereate Test data"

    def handle(self, *args, **options):
        # Generate test data
        self.stdout.write("Deleting old data ...")
        models = [Book, Author, Category, User]

        for model in models:
            model.objects.all().delete()

        self.stdout.write("Creating new data ...")

        checkCategory = CategorySeeding(number_of_categories=NUMBER_OF_CATEGORIES)
        self.stdout.write(
            self.style.SUCCESS(f"Number of categories: {checkCategory} created.")
        )

        # UserSeeding
        checkUser = UserSeeding(number_of_users=NUMBER_OF_USERS)
        self.stdout.write(self.style.SUCCESS(f"Number of Users: {checkUser} created."))

        # BookSeeding
        checkBook = BookSeeding(number_of_books=NUMBER_OF_BOOKS)
        self.stdout.write(self.style.SUCCESS(f"Number of Books: {checkBook} created."))

        # AuthorSeeding
        checkAuthor = AuthorSeeding(
            number_of_authors=NUMBER_OF_AUTHORS, number_of_books=NUMBER_OF_BOOKS
        )
        self.stdout.write(
            self.style.SUCCESS(f"Number of Authors: {checkAuthor} created.")
        )

        self.stdout.write(self.style.SUCCESS("Test data created."))
