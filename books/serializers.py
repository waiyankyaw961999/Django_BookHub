from rest_framework import serializers
from .models import Book, Category


class BookSerializer(serializers.HyperlinkedModelSerializer):

    category = serializers.PrimaryKeyRelatedField(
        source="category.name", read_only=True
    )

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    # def update(self,instance,validated_data):
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.author = validated_data.get('author',instance.author)
    #     instance.published_date = validated_data.get('published_date',instance.published_date)
    #     instance.category = validated_data.get('category',instance.category)
    #     instance.cover_image = validated_data.get('cover_image',instance.cover_image)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.save()
    #     return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
