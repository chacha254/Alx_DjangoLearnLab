from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BooksInLibrary'] = self.object.books.all()
        return context
