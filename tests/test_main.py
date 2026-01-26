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


#.......STEP 1: Use pathlib + json in test_main.py

from pathlib import Path
import json


#.......STEP 2: Locate the project root from test_main.py

# '__file__' will give you the path of test_main.py.
# - From there, we can step “up” one level to reach the project root (library checkout system/), then into data/.
# - Add this in test_main.py (under the imports):

#⬇️ Get the absolute path to the project root (one level up from tests/)
PROJECT_ROOT = Path(__file__).resolve().parents[1] 

#⬇️ Build the full path to data/library_books.json
BOOKS_JSON_PATH = PROJECT_ROOT / "data" / "library_books.json"

# At this point:
# - PROJECT_ROOT → /full/path/to/library checkout system
# - BOOKS_JSON_PATH → /full/path/to/library checkout system/data/library_books.json

# This is OS-independent and doesn’t rely on where you run the script from, which is 
# why this style is used a lot in real projects.


#.......STEP 3: Load the JSON list into Python

#⬇️ Now we read the file and parse it with json.load():
def load_library_books():
    with BOOKS_JSON_PATH.open("r", encoding="utf-8") as f:
        books = json.load(f)
    return books

# Assuming your JSON looks like a top-level list of book 
# dictionaries, books will be a Python list of dict objects.


#.......STEP 4: Use the loaded data in your tests

def test_library_books_loaded():
    books = load_library_books()

    # Basic sanity checks:
    assert isinstance(books, list)
    assert len(books) > 0

    first_book = books[0]
    assert "book_id" in first_book
    assert "title" in first_book
    assert "author" in first_book

    print(books)

test_library_books_loaded()

# This keeps things:
# - simple
# - test-friendly
# - aligned with real-world practices


#.......STEP 5: Quick “why this is industry-standard”

# 1 - pathlib.Path is preferred over manually building strings like "../data/library_books.json" because:
# - it’s cross-platform (Windows, macOS, Linux)
# - it’s more readable (PROJECT_ROOT / "data" / "file.json")

# 2 - Using Path(__file__).resolve().parents[1]:
# - ties your path to the location of the file, not the current working directory
# - makes tests more robust when run via pytest, an IDE, or a CI pipeline

# 3 - Keeping the loading logic in a small helper function (load_library_books) makes it:
# - reusable
# - easy to test
# - easy to change later (e.g., if you move the file)

#---------------------------------------------JSON-Related (+ explanations)⬆️------------------------------------------------



#TODO: 
# Establish this files location relative to the root folder [✅Resolved\Completed]
# - Then establish the means to import the JSON file

