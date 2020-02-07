from django.urls import path
from books.views import ListBooks, NewBook

app_name = 'books'
urlpatterns = [
    path('books/', ListBooks.as_view(), name="index"),
    path('books/new', NewBook.as_view()),
]
