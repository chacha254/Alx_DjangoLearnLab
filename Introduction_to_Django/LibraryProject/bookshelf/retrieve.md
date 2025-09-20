from bookshelf.models import Book

book = Book.objects.get(title="1984")
for field in book._meta.fields:
    print(f"{field.name}: {getattr(book, field.name)}")