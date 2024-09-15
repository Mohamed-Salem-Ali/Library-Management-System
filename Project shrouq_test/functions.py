# transaction.py
from data_handler import save_member
from member import Member

def admin_menu():
    print("\n--- Admin Menu ---")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Display All Books")
    print("4. Register a Member")
    print("5. View All Members")
    print("6. Borrow a Book (for users)")
    print("7. Return a Book (for users)")
    print("8. Save and Exit")

def user_menu():
    print("\n--- User Menu ---")
    print("1. Display All Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View Borrowed Books")
    print("5. Save and Exit")

def create_first_admin(library):
    if len(library.members) == 0:
        print("No members found. Creating an admin account.")
        admin_id = input("Enter Admin ID: ")
        admin_name = input("Enter Admin Name: ")
        admin = Member(admin_id, admin_name, role='admin')
        library.register_member(admin)
        save_member(library)
        print("Admin account created successfully!")
        return admin
    return None

def display_all_books(library):
    if library.books:
        # Print table header
        print("\n--------------------------------------------------- All Books ---------------------------------------------------")
        print(f"{'ID'.ljust(5)} {'Title'.ljust(35)} {'Author'.ljust(30)} {'Genre'.ljust(30)} {'Status'.ljust(10)}")
        print("-" * 113)
        
        # Print each book in a formatted table
        for book in library.books.values():
            status = "Available" if book.available else "Checked Out"
            print(f"{book.book_id.ljust(5)} {book.title.ljust(35)} {book.author.ljust(30)} {book.genre.ljust(30)} {status.ljust(10)}")
    else:
        print("No books available in the library.")

def display_all_members(library):
    if library.members:
        # Print table header
        print("\n----------------- All Members -----------------")
        print(f"{'ID'.ljust(5)} {'Name'.ljust(15)} {'Role'.ljust(10)} {'Borrowed Books'.ljust(30)}")
        print("-" * 47)
        
        # Print each member in a formatted table
        for member in library.members.values():
            borrowed_books = ", ".join(member.borrowed_books) if member.borrowed_books else "None"
            print(f"{member.member_id.ljust(5)} {member.name.ljust(15)} {member.role.ljust(10)} {borrowed_books.ljust(30)}")
    else:
        print("No members registered in the library.")


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