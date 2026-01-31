# from utils import load_library_books

# print(load_library_books())

class Book:
    """
    Displays all available book titles.
    Checks if a specific book is available or not.
    Returns True if it is, False if its not.
    Does not store anything.
    """
    def __init__(self, book_title, book_author, library_data):
        self.book_title = book_title
        self.book_author = book_author
        self.library_data = library_data

    def is_available(self):
        for list_item in self.library_data:
            if list_item["title"] == self.book_title and list_item["author"] == self.book_author:
                print(list_item)



class Library:
    """
    Docstring for Library
    """
    def __init__(self):
        pass

class User:
    """
    Docstring for User
    """
    def __init__(self):
        pass