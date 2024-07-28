from rest_framework.generics import ListAPIView

from library.models import Book
from api.serializers import BookSerializer


class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    