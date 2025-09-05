from django.contrib import admin
from .models import Book

# Customize how Book is shown in the Admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # show these columns in list view
    list_filter = ('author', 'publication_year')             # filters in the sidebar
    search_fields = ('title', 'author')                      # search box

# Register the Book model with its custom admin
admin.site.register(Book, BookAdmin)
