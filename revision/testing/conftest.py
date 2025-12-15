import pytest
from revision.app.classes import Book, Lib

@pytest.fixture(scope='class')
def book():
    return Book(name='test_book1', author='test_author1')

@pytest.fixture(scope='class')
def book2():
    return Book(name='test_book2', author='test_author2')

@pytest.fixture(scope='class')
def library():
    return Lib('test_library1')

