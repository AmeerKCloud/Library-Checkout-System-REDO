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
                if list_item["available"] == True:
                    print(f"\n{self.book_title}, by {self.book_author}, is currently available ✅")
                else:
                    print(f"\n{self.book_title}, by {self.book_author}, is currently unavailable ❌")

class Library:
    """
    Prints the entire list of books.
    Allows user to borrow a book
    or return a book.
    """
    def __init__(self, library_data):
        self.library_data = library_data
        pass

    def show_books(self):
        """
        Displays entire list of books.
        """
        print("\n_______ All of our titles: _______")
        for item in self.library_data:
            for key, value in item.items():
                print(f"{key}: {value}")
            print("------------------------------")

    def borrow_book(self, book_title, book_author):
        """
        Allow user to borrow a book.
        MAke book availability 'False'.
        """
        self.book_title = book_title
        self.book_author = book_author

        for item in self.library_data:
            if item["title"] == self.book_title and item["author"] == self.book_author:
                if item["available"] == True:
                    print(f"You just borrowed {self.book_title}, by {self.book_author}.")
                    new_status = False
                    return new_status, item["book_id"]

    def return_book(self, book_title, book_author):
        """
        Allow user to return a book.
        Make book availability 'True'.
        """
        self.book_title = book_title
        self.book_author = book_author

        for item in self.library_data:
            if item["title"] == self.book_title and item["author"] == self.book_author:
                if item["available"] == False:
                    print(f"You just returned {self.book_title}, by {self.book_author}.")
                    new_status = True
                    return new_status, item["book_id"]

class User:
    """
    Creates and keeps a record of all of
    a users borrowed and returned books.
    """

    user_books_history = {
        "borrowed": {},
        "returned": {},
    }

    def __init__(self, user_name, title, author, date):
        self.user_name = user_name
        self.title = title
        self.author = author
        self.date = date
        pass

    def borrowed_book(self):
        """Makes a list of all of a users borrowed books."""
        



    def returned_book(self):
        """Makes a list of all of a users borrowed books."""