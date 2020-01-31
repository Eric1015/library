from django.urls import path
from books.views import ListBooks, NewBook

urlpatterns = [
    path('books/', ListBooks.as_view()),
    path('books/new', NewBook.as_view()),
]
