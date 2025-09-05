from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library   # ✅ must include Library explicitly

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):   # ✅ uses DetailView
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
