# main.py

from book import Book
from member import Member
from library import Library
from transaction import borrow_book, return_book
from data_handler import save_data, load_data

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
        save_data(library)
        print("Admin account created successfully!")
        return admin
    return None

def display_all_books(library):
    if library.books:
        # Print table header
        print("\n--- All Books ---")
        print(f"{'ID'.ljust(5)} {'Title'.ljust(20)} {'Author'.ljust(20)} {'Genre'.ljust(15)} {'Status'.ljust(10)}")
        print("-" * 70)
        
        # Print each book in a formatted table
        for book in library.books.values():
            status = "Available" if book.available else "Checked Out"
            print(f"{book.book_id.ljust(5)} {book.title.ljust(20)} {book.author.ljust(20)} {book.genre.ljust(15)} {status.ljust(10)}")
    else:
        print("No books available in the library.")

def display_all_members(library):
    if library.members:
        # Print table header
        print("\n--- All Members ---")
        print(f"{'ID'.ljust(5)} {'Name'.ljust(15)} {'Role'.ljust(10)} {'Borrowed Books'.ljust(30)}")
        print("-" * 60)
        
        # Print each member in a formatted table
        for member in library.members.values():
            borrowed_books = ", ".join(member.borrowed_books) if member.borrowed_books else "None"
            print(f"{member.member_id.ljust(5)} {member.name.ljust(15)} {member.role.ljust(10)} {borrowed_books.ljust(30)}")
    else:
        print("No members registered in the library.")

def main():
    library = load_data()  # Load existing data

    # Check if there are any members, if not create an admin
    member = create_first_admin(library)

    # If admin already exists, proceed to login
    while True:
        if not member:
            member_id = input("Enter your Member ID: ")
            member = library.members.get(member_id)
        if not member:
            print("Member not found.")
        else:
            break
    while True:
        # Check role and display the appropriate menu
        
        if member.role == 'admin':
            admin_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                genre = input("Genre: ")
                book = Book(book_id, title, author, genre)
                library.add_book(book)
                
            elif choice == '2':
                book_id = input("Enter Book ID to remove: ")
                library.remove_book(book_id)
                
            elif choice == '3':
                display_all_books(library)
                
            elif choice == '4':
                member1=member
                member_id = input("Member ID: ")
                name = input("Member Name: ")
                role = input("Role (admin/user): ")
                member = Member(member_id, name, role)
                library.register_member(member)
                member=member1
                
            elif choice == '5':
                display_all_members(library)
                
            elif choice == '6':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                borrow_book(library, user_id, book_id)

            elif choice == '7':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                return_book(library, user_id, book_id)

            elif choice == '8':
                save_data(library)
                break

        elif member.role == 'user':
            user_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                book_id = input("Book ID: ")
                borrow_book(library, member.member_id, book_id)

            elif choice == '2':
                book_id = input("Book ID: ")
                return_book(library, member.member_id, book_id)

            elif choice == '3':
                if member.borrowed_books:
                    print("Your borrowed books:")
                    for book_id in member.borrowed_books:
                        if book_id in library.books:
                            book = library.books[book_id]
                            print(f"{book.book_id} - {book.title} by {book.author}")
                    if not any(book_id in library.books for book_id in member.borrowed_books):
                        print("None of your borrowed books are currently available in the library.")
                else:
                    print("You have not borrowed any books.")
            elif choice == '4':
                save_data(library)
                break
            
if __name__ == "__main__":
    main()