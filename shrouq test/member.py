# member.py
import datetime
class Member:
    def __init__(self, member_id, name, role='user', borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.role = role
        self.borrowed_books = [book_id for book_id in borrowed_books if book_id] if borrowed_books else []
        
    def borrow_book(self, book,member):
        if book.available:
            self.borrowed_books.append(book.book_id)
            book.available = False
            current_date=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
            print(f"The '{book.title}' book is borrowed by {self.name} on {current_date}")
        else:
            print(f"The {book.title} book is already borrowed to {member.name} on {current_date}")

    def return_book(self, book):
        if book.book_id in self.borrowed_books:
            self.borrowed_books.remove(book.book_id)
            book.available = True
            current_date=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
            print(f"The '{book.title}' book is returned by {self.name} on {current_date}")
        else:
            print(f"{self.name} did not borrow this book.")
