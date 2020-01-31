from django import forms
from books.models import Book

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_at', 'genre', 'num_of_pages')