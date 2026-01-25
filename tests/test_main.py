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


#---------------------------------------------⬇️JSON-Related (+ explanations)------------------------------------------------

# # ______PROJECT STRUCTURE______:
# Let’s assume your folder layout looks like this:

# library checkout system/
# ├── data/
# │ └── library_books.json
# ├── tests/
# │ └── test_main.py
# └── (other project files, e.g. src/, README, etc.)

# Our goal:
# In tests/test_main.py, load the list from data/library_books.json in a robust way.

from pathlib import Path
import json


# '__file__' will give you the path of test_main.py.
# From there, we can step “up” one level to reach the project root (library checkout system/), then into data/.
# - Add this in test_main.py (under the imports):

# Get the absolute path to the project root (one level up from tests/)
PROJECT_ROOT = Path(__file__).resolve().parents[1] 



#---------------------------------------------JSON-Related (+ explanations)⬆️------------------------------------------------



#TODO: 
# Establish this files location relative to the root folder
# - Then establish the means to import the JSON file

