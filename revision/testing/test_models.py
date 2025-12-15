import pytest
from revision.app.classes import Book, Lib

class TestBook1:

    def test_name(self, book):
        assert book.name == 'test_book1'
        assert book.author == 'test_author1'

class TestBook2:

    def test_name(self, book2):
        assert book2.name == 'test_book2'
        assert book2.author == 'test_author2'

class TestBookIDs:

    def test_uniqueness(self, book, book2):
        assert book.id != book2.id

class TestLibrary:

    def test_lib(self, library, book):
        assert library.libname == 'test_library1'
        assert library.booklist == []
        library.add_book(book)
        assert library.booklist == [book]
        library.remove_book(book.id)
        assert library.booklist == []