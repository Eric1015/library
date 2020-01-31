from django.shortcuts import render, redirect
from django import views
from books.forms import CreateBookForm

# Create your views here.
class ListBooks(views.View):
    def get(self, request, *args, **kwargs):
        context = {'message': 'Hello world'}
        return render(request, 'books/index.html', context)

    def post(self, request, *args, **kwargs):
        return redirect(reverse('books:index'))

class NewBook(views.View):
    def get(self, request, *args, **kwargs):
        context = {'form': CreateBookForm()}
        return render(request, 'books/form.html', context)