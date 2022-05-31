import random
from faker import Faker
import faker.providers
from books.models import Category

Categories = [
    "Technology",
    "Business",
    "Story",
    "Entertainment",
    "Health",
    "Science",
]


class CategoriesProvider(faker.providers.BaseProvider):
    def category(self):
        return random.choice(Categories)


fake = Faker()
fake.add_provider(CategoriesProvider)


def CategorySeeding(number_of_categories=6):
    for i in range(1, number_of_categories):
        d = fake.unique.category()
        Category.objects.create(id=i, name=d, description=fake.text(max_nb_chars=100))
    checkCategory = Category.objects.all().count()
    return checkCategory
