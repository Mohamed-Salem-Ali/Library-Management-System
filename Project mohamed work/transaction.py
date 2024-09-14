# transaction.py

def borrow_book(library, member_id, book_id):
    member = library.members.get(member_id)
    book = library.books.get(book_id)

    if not member:
        print(f"Member with ID {member_id} not found.")
    elif not book:
        print(f"Book with ID {book_id} not found.")
    elif not book.available:
        print(f"Book '{book.title}' is already borrowed.")
    else:
        member.borrow_book(book)

# Return Book Function
def return_book(library, member_id, book_id):
    member = library.members.get(member_id)
    book = library.books.get(book_id)

    if not member:
        print(f"Member with ID {member_id} not found.")
    elif not book:
        print(f"Book with ID {book_id} not found.")
    elif book.available:
        print(f"Book '{book.title}' was not borrowed.")
    else:
        member.return_book(book)