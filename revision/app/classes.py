import uuid


class Book:
    def __init__(self, author, name):
        self.author = author
        self.name = name
        self.id = uuid.uuid4().hex

    def __str__(self):
        return f'book - {self.name}, author - {self.author}'

    def __repr__(self):
        return f'book({self.name}-{self.author}, {self.id})'

class Lib:
    def __init__(self, libname: str):
        self.libname = libname
        self.booklist = []

    def add_book(self, book: Book):
        self.booklist.append(book)

    def remove_book(self, book_id):
        for book in self.booklist:
            if book_id == book.id:
                self.booklist.remove(book)


    def get_books(self):
        return self.booklist


book1 = Book('George Orwell', '1984')
book2 = Book('merzlyak', 'geometriya')
library = Lib('library')

library.add_book(book2)
library.add_book(book1)

print(library.get_books())
library.remove_book(book1.id)
print(library.get_books())

