from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}  # Stores all books in a dictionary with book_id as key
        self.members = {}  # Stores all members in a dictionary with member_id as key

    def add_book(self, book):
        if book.book_id in self.books:
            print(f"Book with ID {book.book_id} already exists.")
        else:
            self.books[book.book_id] = book
            print(f"Added book: {book.title}")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed book: {removed_book.title}")
            
            # Remove the book from all members' borrowed_books lists
            for member in self.members.values():
                if book_id in member.borrowed_books:
                    member.borrowed_books.remove(book_id)
                    print(f"Removed book ID {book_id} from {member.name}'s borrowed books.")
        else:
            print("Book not found.")

    def register_member(self, member):
        if member.member_id in self.members:
            print(f"Member with ID {member.member_id} already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Registered member: {member.name}")