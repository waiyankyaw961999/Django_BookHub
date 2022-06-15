from faker import Faker
from accounts.models import User
from django.contrib.auth.hashers import make_password


fake = Faker()


def UserSeeding(number_of_users=50):

    User.objects.create(
        id=1,
        username="waiyan",
        email="wykdev@gmail.com",
        password=make_password("password"),
        is_email_verified=True,
        is_active=True,
        is_staff=True,
    )
    for i in range(1, number_of_users):
        User.objects.create(
            id=i + 1,
            username=fake.email().split("@")[0],
            password=make_password("password"),
            email=fake.email(),
            is_email_verified=True,
            is_active=True,
            is_staff=False,
        )
    checkCategory = User.objects.all().count()
    return checkCategory
