from django.db import models


class Book(models.Model):
    name = models.TextField(blank=True)
    author = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Book"
