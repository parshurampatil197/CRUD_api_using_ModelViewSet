from rest_framework import serializers
from ..models.book_models import Book


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    author = serializers.CharField(allow_null=False, allow_blank=False, required=True)

    class Meta:
        model = Book
        fields = '__all__'
