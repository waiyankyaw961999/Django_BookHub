from rest_framework import serializers
from .models import Author
from accounts.serializers import UserSerializer


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ["id", "user", "first_name", "last_name", "bio"]
