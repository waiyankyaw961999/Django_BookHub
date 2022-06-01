from django.db import models
from accounts.models import User

# Create your models here.
class Author(models.Model):
    """
    Author Models \n
    |- id (PK) -|- first_name -|- last_name -|- created_at -|- updated_at -|
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
