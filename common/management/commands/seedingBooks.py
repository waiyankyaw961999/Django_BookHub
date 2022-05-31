from datetime import datetime
import random
from faker import Faker
import faker.providers
from books.models import Book
from django.utils.timezone import get_current_timezone

fake = Faker()


def BookSeeding(number_of_books=20):

    for i in range(1, number_of_books):
        book = Book.objects.create(
            id=i,
            title=fake.text(max_nb_chars=20),
            published_date=datetime.now(tz=get_current_timezone()),
            description=fake.text(max_nb_chars=100),
            cover_image=fake.image_url(width=100, height=400),
            category_id=random.randint(1, 5),
        )

    checkBook = Book.objects.all().count()
    return checkBook
