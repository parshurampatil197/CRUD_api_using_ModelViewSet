from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Author"


class Book(models.Model):
    title = models.TextField(blank=True)
    pages = models.IntegerField(blank=True, default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Book"

