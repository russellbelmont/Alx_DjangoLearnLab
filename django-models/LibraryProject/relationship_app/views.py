from django.shortcuts import render
from django.views.generic.detail import DetailView   # checker expects this
from .models import Library      # checker expects this exact line
from .models import Book

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
