from django.contrib import admin
from .models import Book, Borrower

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower)
