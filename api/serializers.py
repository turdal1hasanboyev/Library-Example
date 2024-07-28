from rest_framework import serializers

from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'subtitle', 'title', 'author', 'isbn')

        extra_kwargs = {
            "id": {"read_only": True},
        }
