# from utils import load_library_books

# print(load_library_books())

class Book:
    """
    Displays all available book titles.
    Checks if a specific book is available or not.
    Returns True if it is, False if its not.
    Does not store anything.
    """
    def __init__(self, book_title, book_author, json_library_data):
        self.book_title = book_title
        self.book_author = book_author
        self.json_library_data = json_library_data

    def is_available(self):
        for list_item in self.json_library_data:
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
    def __init__(self, json_library_data):
        self.json_library_data = json_library_data
        pass

    def show_books(self):
        """
        Displays entire list of books.
        """
        print("\n_______ All of our titles: _______")
        for item in self.json_library_data:
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

        len_library_data = len(self.json_library_data)

        while True:
            for item in self.json_library_data:
                if item["title"] == self.book_title and item["author"] == self.book_author:
                    if item["available"] == True:
                        print(f"You just borrowed {self.book_title}, by {self.book_author}.")
                        new_status = False
                        return new_status, item["book_id"]
                else:
                    len_library_data -= 1
                    print(len_library_data)
            if len_library_data < 0:
                print(f"\nSorry, we were unable to find {self.book_title}, by {self.book_author}.")
                print("Perhaps check your spelling or review our available list?")
                break



    def return_book(self, book_title, book_author):
        """
        Allow user to return a book.
        Make book availability 'True'.
        """
        self.book_title = book_title
        self.book_author = book_author

        for item in self.json_library_data:
            if item["title"] == self.book_title and item["author"] == self.book_author:
                if item["available"] == False:
                    print(f"You just returned {self.book_title}, by {self.book_author}.")
                    new_status = True
                    return new_status, item["book_id"]
            else:
                print(f"\nSorry, we were unable to find {self.book_title}, by {self.book_author}.")
                print("Perhaps check your spelling or review our available list?")

class User:
    """
    Creates and keeps a record of all of
    a users borrowed and returned books.
    """

    user_books_history = {
        "borrowed": {},
        "returned": {},
    }

    def __init__(self):
        pass

    def borrowed_book(self, user_name, book_title, book_author, todays_date, json_library_data):
        """Makes a list of all of a users borrowed books."""
        self.user_name = user_name
        self.book_title = book_title
        self.book_author = book_author
        self.todays_date = todays_date
        self.json_library_data = json_library_data

        if self.user_name not in User.user_books_history["borrowed"]:
            User.user_books_history["borrowed"][self.user_name] = []            #⬅️ Initiates empty list

        borrowed_book_dict = {}                                                 #⬅️ Initiates borrowed books dict to be appended to empty list

        for item in self.json_library_data:
            if item["title"] == self.book_title and item["author"] == self.book_author:
                for key, value in item.items():
                    borrowed_book_dict[key] = value
                User.user_books_history["borrowed"][self.user_name].append(borrowed_book_dict)
        print(User.user_books_history)

    def view_borrowed_history(self, user_name):
        self.user_name = user_name

        if self.user_name not in User.user_books_history["borrowed"]:
            print(f"\nSorry, {self.user_name} has no currently borrowed books to show. ☹️")
        else:
            print(f"---------- All currently borrowed books for {self.user_name} ----------:")
            for item in User.user_books_history["borrowed"][self.user_name]:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("_________________________")

    def returned_book(self, user_name, book_title, book_author, todays_date, json_library_data):
        """Makes a list of all of a users borrowed books."""
        self.user_name = user_name
        self.book_title = book_title
        self.book_author = book_author
        self.todays_date = todays_date
        self.json_library_data = json_library_data

        if self.user_name not in User.user_books_history["returned"]:
            User.user_books_history["returned"][self.user_name] = []            #⬅️ Initiates empty list

        returned_book_dict = {}                                                 #⬅️ Initiates returned books dict to be appended to empty list

        for item in self.json_library_data:
            if item["title"] == self.book_title and item["author"] == self.book_author:
                for key, value in item.items():
                    returned_book_dict[key] = value
                User.user_books_history["returned"][self.user_name].append(returned_book_dict)
        print(User.user_books_history)

    def view_returned_history(self, user_name):
        self.user_name = user_name

        if self.user_name not in User.user_books_history["returned"]:
            print(f"\nSorry, {self.user_name} has no currently returned books to show. ☹️")
        else:
            print(f"---------- All currently returned books for {self.user_name} ----------:")
            for item in User.user_books_history["returned"][self.user_name]:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("_________________________")

# NOTE: Progress Report:
# Currently @ 'Library' class, @ 'borrow_book' function trying to figure out how to borrow book & do countdown.