# data_handler.py
import json
from book import Book
from member import Member
from library import Library

def save_data(library):
    # Save books
    with open('books_data.txt', 'w') as book_file:
        for book in library.books.values():
            book_file.write(f"{book.book_id},{book.title},{book.author},{book.genre},{book.available}\n")

    # Save members
    with open('members_data.txt', 'w') as member_file:
        for member in library.members.values():
            borrowed_books_str = ",".join(member.borrowed_books)  # Convert list to a comma-separated string
            member_file.write(f"{member.member_id},{member.name},{member.role},{borrowed_books_str}\n")

    print("Data saved successfully to text files.")

# data_handler.py

def load_data():
    library = Library()

    try:
        # Load books
        with open('books_data.txt', 'r') as book_file:
            for line in book_file:
                book_data = line.strip().split(',')  # Split by commas
                book_id, title, author, genre, available = book_data
                available = available == 'True'  # Convert string back to boolean
                book = Book(book_id, title, author, genre, available)
                library.books[book_id] = book

        # Load members
        with open('members_data.txt', 'r') as member_file:
            for line in member_file:
                member_data = line.strip().split(',')  # Split by commas
                member_id = member_data[0]
                name = member_data[1]
                role = member_data[2]
                borrowed_books = member_data[3:]  # The rest are borrowed books (optional)
                member = Member(member_id, name, role, borrowed_books)
                library.members[member_id] = member

        print("Library data loaded successfully from text files.")
        return library

    except FileNotFoundError:
        print("No previous data found. Starting with an empty library.")
        return Library()