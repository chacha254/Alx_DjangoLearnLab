from models import Book, Author, Library, Librarian
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()
 
Library.objects.get(name=Library_name)
books.all()

book = Book(title="TheGrind", author="SirCharles")
book2 = Book(title="Hustle", author="Mie")
books = Book.objects.filter(attribute="Author")
books = Book.objects.all()

