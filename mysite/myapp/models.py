from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=120)


class Reader(models.Model):
    name = models.CharField(max_length=120)


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.ManyToManyField(Author)
    book_reserved = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True)