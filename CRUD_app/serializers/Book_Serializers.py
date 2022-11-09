from rest_framework import serializers
from ..models.book_models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    # pages = serializers.IntegerField(default=0, allow_null=True)
    # author = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'pages', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    # gender = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    book = serializers.StringRelatedField(many=True, read_only=True)
    # book = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # book = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # book = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')

    class Meta:
        model = Author
        fields = ['id', 'name', 'gender', 'book']


