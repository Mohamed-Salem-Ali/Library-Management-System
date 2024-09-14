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
    print("3. Register a Member")
    print("4. View All Members")
    print("5. Borrow a Book (for users)")
    print("6. Return a Book (for users)")
    print("7. Save and Exit")

def user_menu():
    print("\n--- User Menu ---")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. View Borrowed Books")
    print("4. Save and Exit")

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
                member1=member
                member_id = input("Member ID: ")
                name = input("Member Name: ")
                role = input("Role (admin/user): ")
                member = Member(member_id, name, role)
                library.register_member(member)
                member=member1
            elif choice == '4':
                print("All registered members:")
                member1=member
                for member in library.members.values():
                    print(f"{member.member_id}: {member.name} ({member.role})")
                member = member1
            elif choice == '5':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                borrow_book(library, user_id, book_id)

            elif choice == '6':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                return_book(library, user_id, book_id)

            elif choice == '7':
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