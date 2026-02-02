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



from modules.utils import load_library_books, update_library_books_availability
from modules.models import Book, Library

# print(load_library_books())

while True:
    name = input("\nEnter your name to begin:\n").title()
    if name == "E":
        break
    while True:
        library = Library(load_library_books())
        user_choice = input("\nEnter one of the following:\n'a' for availability\n'b' for borrow\n'r' for return\n'v' for viewing all titles\n'e' to exit:\n").lower()

        if user_choice == 'a':
            title = input("Enter book title:\n").upper()
            author = input("Enter authors name:\n").upper()

            book = Book(title, author, load_library_books())
            book.is_available()

        elif user_choice == 'b':
            title = input("\nEnter book title:\n").upper()
            author = input("Enter author name:\n").upper()
            new_status, book_id = library.borrow_book(book_title=title, book_author=author)
            update_library_books_availability(update_status=new_status, id_book=book_id)

        elif user_choice == 'r':
            title = input("\nEnter book title:\n").upper()
            author = input("Enter author name:\n").upper()
            new_status, book_id = library.return_book(book_title=title, book_author=author)
            update_library_books_availability(update_status=new_status, id_book=book_id)

        elif user_choice == 'v':
            library.show_books()
            pass

        else:
            break


