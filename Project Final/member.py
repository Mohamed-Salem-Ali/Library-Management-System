# member.py

class Member:
    def __init__(self, member_id, name, role='user', borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.role = role
        self.borrowed_books = borrowed_books if borrowed_books else []  # Default to an empty list if None
        
    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book.book_id)
            book.available = False
            print(f"{self.name} successfully borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book.book_id in self.borrowed_books:
            self.borrowed_books.remove(book.book_id)
            book.available = True
            print(f"{self.name} successfully returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow this book.")
