# transaction.py

def borrow_book(library, member_id, book_id):
    member = library.members.get(member_id)
    book = library.books.get(book_id)

    if member and book:
        member.borrow_book(book)
    else:
        print("Member or Book not found.")

def return_book(library, member_id, book_id):
    member = library.members.get(member_id)
    book = library.books.get(book_id)

    if member and book:
        member.return_book(book)
    else:
        print("Member or Book not found.")