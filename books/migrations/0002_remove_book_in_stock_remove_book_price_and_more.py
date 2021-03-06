# Generated by Django 4.0 on 2022-05-31 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0001_initial"),
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="in_stock",
        ),
        migrations.RemoveField(
            model_name="book",
            name="price",
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(blank=True, null=True, to="authors.Author"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
