from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    # ✅ render with full path to template
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ full path
    context_object_name = "library"
