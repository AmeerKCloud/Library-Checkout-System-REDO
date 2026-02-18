# All helper classes go here


from datetime import datetime

#---------------------------------------------⬇️JSON-Related (+ explanations)------------------------------------------------

# ______PROJECT STRUCTURE______:
# Let’s assume your folder layout looks like this:

# library checkout system/
# ├── data/
# │ └── library_books.json
# ├── src/
# │ └── modules/
# |   └── utils.py
# └── (other project files, e.g. tests/, README, etc.)

# Our goal:
# In tests/test_main.py, load the list from data/library_books.json in a robust way.


#.......STEP 1: Use pathlib + json in test_main.py

from pathlib import Path
import json


#.......STEP 2: Locate the project root from test_main.py

# '__file__' will give you the path of test_main.py.
# - From there, we can step “up” one level to reach the project root (library checkout system/), then into data/.
# - Add this in test_main.py (under the imports):

#⬇️ Get the absolute path to the project root (two levels up from modules/src/)
PRJECT_ROOT = Path(__file__).resolve().parents[2] 

#⬇️ Build the full path to data/library_books.json (where the library list of book dict objects exists)
BOOKS_JSON_PATH = PRJECT_ROOT / "data" / "library_books.json"

# At this point:
# - PRJECT_ROOT → /full/path/to/library checkout system
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

#.......STEP 3.5 (my own addition): Update JSON book objects with new status.
def update_library_books_availability(update_status, id_book):
    with BOOKS_JSON_PATH.open("r", encoding="utf-8") as f:
        books = json.load(f)
    
    for book in books:
        if book["book_id"] == id_book:
            book["available"] = update_status
    
    with BOOKS_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(books, f, indent=2)

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

#     print(books)                      #⬅️ For testing purposes

# test_library_books_loaded()

# This keeps things:
# - simple
# - test-friendly
# - aligned with real-world practices


#.......STEP 5: Quick “why this is industry-standard”

# 1 - pathlib.Path is preferred over manually building strings like "../data/library_books.json" because:
# - it’s cross-platform (Windows, macOS, Linux)
# - it’s more readable (PRJECT_ROOT / "data" / "file.json")

# 2 - Using Path(__file__).resolve().parents[2]:
# - ties your path to the location of the file, not the current working directory
# - makes tests more robust when run via pytest, an IDE, or a CI pipeline

# 3 - Keeping the loading logic in a small helper function (load_library_books) makes it:
# - reusable
# - easy to test
# - easy to change later (e.g., if you move the file)

#---------------------------------------------JSON-Related (+ explanations)⬆️------------------------------------------------

class UserInputs:

    def user_name(self):
        while True:
            name = input("\nEnter your name to begin:\n").title()

            if name != "":
                return name
            print("Field cannot be empty ❌")

    def book_title(self):
        while True:
            title = input("Enter book title:\n").upper()

            if title != "":
                return title
            print("Field cannot be empty ❌")

    def book_author(self):
        while True:
            author = input("Enter authors name:\n").upper()

            if author != "":
                return author
            print("Field cannot be empty ❌")


    def date(self):                                         #⬅️ Currently working on date
        date_format = "%m/%d/%y"

        while True:
            self.user_date_input = input("Enter todays date (MM/DD/YYYY):\n")

            if self.user_date_input == "e":
                break

            if self.user_date_input != "":
                try:
                    # step 1: verify format
                    print("\n'try' is working")
                    parsed_date = datetime.strptime(self.user_date_input, date_format)
                    print(f"\nParsed date: {parsed_date}")

                    # Step 2: force correct format
                    if parsed_date:
                        formatted_date = parsed_date.strftime(date_format)

                        # Step 3: return formatted date string
                        print(f"Formatted date: {formatted_date}")
                        return formatted_date
                    else:
                        print("❌ Invalid date format. Try again.")
                except ValueError:
                    print("❌ Invalid format. Please use MM/DD/YYYY.")
            else:
                print("Field cannot be left blank.")


    def menu_1(self, name):
        self.name = name
        while True:
            choice = input(f"\n{self.name}, enter one of the following:\n'a' for availability\n'b' for borrow\n'r' for return\n'v' for viewing all titles\n'h' for currently returned or borrowed books\n'e' to exit:\n").lower()

            if choice in ["a", "b", "r", "v", "h", "e"]:
                return choice
            print("\nIncorrect entry ❌")
            print("Please only enter one of the letter choices provided above!")

    def menu_2(self):
        while True:
            choice = input("\nChoose one of the following:\n'b' to view currently borrowed titles\n'r' to view all returned titles:\n").lower()

            if choice in ["b", "r", "e"]:
                return choice
            print("\nIncorrect entry ❌")
            print("Please only enter one of the letter choices provided above!")