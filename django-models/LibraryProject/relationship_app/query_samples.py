from models import Book, Author, Library, Librarian
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()
 

books.all()

library = Library.objects.get(name=library_name)

Book.objects.filter(name="Charles")


book = Book(title="TheGrind", author="SirCharles")
book2 = Book(title="Hustle", author="Mie")
books = Book.objects.filter(attribute="Author")
books = Book.objects.all()

