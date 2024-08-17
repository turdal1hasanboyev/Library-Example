from rest_framework import serializers

from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'subtitle', 'title', 'author', 'isbn', "created_at")

        extra_kwargs = {
            'created_at': {'read_only': True},
            'id': {'read_only': True},
        }
