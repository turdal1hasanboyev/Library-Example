from django.urls import path
from library.views import BookListView


urlpatterns = [
    path('', BookListView.as_view(), name='home')
]
