# data_handler.py
import json
from book import Book
from member import Member
from library import Library

def save_data(library):
    books_data = {book_id: book.__dict__ for book_id, book in library.books.items()}
    members_data = {member_id: member.__dict__ for member_id, member in library.members.items()}

    with open('library_data.json', 'w') as file:
        json.dump({"books": books_data, "members": members_data}, file)

def load_data():
    try:
        with open('library_data.json', 'r') as file:
            data = json.load(file)

            library = Library()
            for book_id, book_info in data['books'].items():
                book = Book(**book_info)
                library.books[book_id] = book

            for member_id, member_info in data['members'].items():
                member = Member(**member_info)
                library.members[member_id] = member

            print("Library data loaded successfully.")
            return library
    except FileNotFoundError:
        print("No previous data found. Starting with an empty library.")
        return Library()