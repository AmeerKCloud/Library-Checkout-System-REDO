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



from modules.utils import UserInputs, load_library_books, update_library_books_availability
from modules.models import Book, Library, User

user_inputs = UserInputs()

while True:
    name = user_inputs.user_name()
    if name == "E":
        break

    user = User()             #⬅️ Create the class object

    while True:
        library = Library(load_library_books())   #⬅️ Moved inside 2nd while-loop otherwise updated json data is NOT renewed inside program

        menu_1_choice = user_inputs.menu_1(name)

        if menu_1_choice == 'a':
            title = input("Enter book title:\n").upper()
            author = input("Enter authors name:\n").upper()
            book = Book(title, author, load_library_books())
            book.is_available()

        elif menu_1_choice == 'b':
            title = input("\nEnter book title:\n").upper()
            author = input("Enter author name:\n").upper()
            date = input("Enter todays date:\n")
            new_status, book_id = library.borrow_book(book_title=title, book_author=author)

            if new_status != None and book_id != None:
                update_library_books_availability(update_status=new_status, id_book=book_id)
                user.borrowed_book(name, title, author, date, load_library_books())
            else:
                print("\nCome back as None")

        elif menu_1_choice == 'r':
            title = input("\nEnter book title:\n").upper()
            author = input("Enter author name:\n").upper()
            date = input("Enter todays date:\n")
            new_status, book_id = library.return_book(book_title=title, book_author=author)
            
            if new_status != None and book_id != None:
                update_library_books_availability(update_status=new_status, id_book=book_id)
                user.returned_book(name, title, author, date, load_library_books())

        elif menu_1_choice == 'v':
            library.show_books()

        elif menu_1_choice == 'h':

            while True:
                menu_2_choice = user_inputs.menu_2()
                if menu_2_choice == 'b':
                    user.view_borrowed_history(user_name=name)
                elif menu_2_choice == 'r':
                    user.view_returned_history(user_name=name)
                else:
                    break

        else:
            break




# TODO: 
# Need to add date functionality to main program.
# - Also need to add it to 'borrowed_book', 'view_borrowed_history', 'returned_book', 'view_returned_history' in the User class.

# Need to add additional menu functionalities
# - Then transfer them to the utils.py file in their own 'inputs' class.

# Need to condense code as practically as is possible.

# Need functionality that removed book from borrowed history once its returned(& vice versa?)

# ---------------------Progress report-----------------------:

# 1) BUG: Fixing 'return_book()' funct inside 'Library' class
# > It's not matching user-entered title and author with what is on the JSON data base
# > > Keeps triggering the 'else' statement in conditional statement.
# > > The problem appears to be that the availability of the borrowed book in the version 
# of the json data saved within the 'return_book()' funct. doesn't change from 'True' to 
# 'False' in order for the logic within the funct. to check for it and return it.
# > > > IMPORTANT: Find out what is causing this.
# RESOLVED: Issue was that 'library = Library(load_library_books())', AKA JSON data input, was outside of 2nd while-loop in main program
# > This was not allowing the updated JSON data file to be accessed by the code within the 2nd while loop
# > Because the JSON data would only load once from the 1st while-loop & be updated once by the code in the 2nd while-loop
# > But because only the 2nd while-loop would loop over again, the updated JSON data would not load
# > Only the old JSON data would remain accessed within the 2nd while-loop, causing the mis-match in availability when trying to return.

# 2) Date input: Currently here
# - Trying to find a way to include borrowed & returned dates to user book history (RESOLVED ✅)
# - Need to now include 'date' module and input formatting to 'utils.py'

# 3) When 'borrowed' books history becomes empty, it should show: 'Sorry, {self.user_name} has no currently borrowed books to show. ☹️'
# - Currently, it only prints this in the beginning before the user even borrows any book
# - But when he does borrow a book and then returns it & 'borrowed books history' becomes empty, it no longer prints this, but prints an empty format

# 4) Add finishing touches to the program:
# - Clean up the code and condense it where possible.
# - 
