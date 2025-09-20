book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book.refresh_from_db()
print(book.title)
# Nineteen Eighty-Four