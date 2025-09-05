from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """Function-based view to list all books"""
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """Class-based view to display library details"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'