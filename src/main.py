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
from modules.models import Book, Library, User

# print(load_library_books())

while True:
    name = input("\nEnter your name to begin:\n").title()
    if name == "E":
        break

    library = Library(load_library_books())             #⬅️ Create the class objects.
    user = User()

    while True:
        menu_1_options = input("\nEnter one of the following:\n'a' for availability\n'b' for borrow\n'r' for return\n'v' for viewing all titles\n'c' for currently returned or borrowed books\n'e' to exit:\n").lower()

        if menu_1_options == 'a':
            title = input("Enter book title:\n").upper()
            author = input("Enter authors name:\n").upper()
            book = Book(title, author, load_library_books())
            book.is_available()

        elif menu_1_options == 'b':
            title = input("\nEnter book title:\n").upper()
            author = input("Enter author name:\n").upper()
            date = input("Enter todays date:\n")
            new_status, book_id = library.borrow_book(book_title=title, book_author=author)

            if new_status != False and book_id != False:
                update_library_books_availability(update_status=new_status, id_book=book_id)
                user.borrowed_book(name, title, author, date, load_library_books())
            else:
                break

        elif menu_1_options == 'r':
            title = input("\nEnter book title:\n").upper()
            author = input("Enter author name:\n").upper()
            date = input("Enter todays date:\n")
            new_status, book_id = library.return_book(book_title=title, book_author=author)
            
            if new_status != False and book_id != False:
                update_library_books_availability(update_status=new_status, id_book=book_id)
                user.returned_book(name, title, author, date, load_library_books())
            else:
                break

        elif menu_1_options == 'v':
            library.show_books()

        elif menu_1_options == 'c':

            while True:
                menu_2_options = input("Choose one of the following:\n'b' to view currently borrowed titles\n'r' to view all returned titles:\n").lower()
                if menu_2_options == 'b':
                    user.view_borrowed_history(user_name=name)
                elif menu_2_options == 'r':
                    user.view_returned_history(user_name=name)

        else:
            break




# TODO: 
# Need to add date functionality to main program.
# - Also need to add it to 'borrowed_book', 'view_borrowed_history', 'returned_book', 'view_returned_history' in the User class.

# Need to add additional menu functionalities
# - Then transfer them to the utils.py file in their own 'inputs' class.

# Need to condense code as practically as is possible.
