# Library Checkout System (OOP + Dictionaries + Modular Design)
# Project Description
# Simulate a simple library where users can borrow and return books.

# Requirements
# Your final program must:
# ✓ Include a Book class
# - Title, author, available (boolean)
# ✓ Include a Library class
# - Stores books in a dictionary: {book_id: Book_object}
# - Methods: show_books(), borrow_book(), return_book()
# ✓ Include a User class
# - Tracks borrowed books
# - Method: borrow(), return_book()
# ✓ Use user input for:
# - Selecting books
# - Borrowing
# - Returning
# ✓ Use modules
# - models.py — classes
# - library_data.py — starting book list
# - main.py — main loop



from modules.utils import load_library_books
from modules.models import Book

# print(load_library_books())

while True:
    user_choice = input("Enter one of the following:\n'a' for availability\n'b' for borrow\n'r' for return\n'v' for viewing all titles\n'e' to exit:\n").lower()

    if user_choice == 'a':
        title = input("Enter book title:\n").upper()
        author = input("Enter authors name:\n").upper()

        book = Book(title, author, load_library_books())
        book.is_available()

    elif user_choice == 'b':
        pass

    elif user_choice == 'r':
        pass

    else:
        break


