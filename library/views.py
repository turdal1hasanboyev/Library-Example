from django.shortcuts import render, redirect
from django.views.generic import ListView
from library.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/booklist.html'
