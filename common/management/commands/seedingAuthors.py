import random
from faker import Faker
import faker.providers
from authors.models import Author
from books.models import Book

fake = Faker()


def AuthorSeeding(number_of_authors=20, number_of_books=20):

    for i in range(1, number_of_authors):
        author = Author.objects.create(
            id=i,
            user_id=i,
            first_name=fake.first_name(),
            bio=fake.text(max_nb_chars=80),
            last_name=fake.last_name(),
        )
        Book.objects.get(id=random.randint(1, number_of_books - 1)).author.add(author)

    checkAuthor = Author.objects.all().count()
    return checkAuthor
