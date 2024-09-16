# main.py

from book import Book
from member import Member
from library import Library
from functions import *
from data_handler import *

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
                display_all_books(library)
                
            elif choice == '2':
                display_all_books(library)
                book_id = input("Enter Book ID to remove: ")
                library.remove_book(book_id)
                
            elif choice == '3':
                display_books_menu(library)

            elif choice == '4':
                filter_by_genre(library)

            elif choice == '5':
                Search_books(library)
                
            elif choice == '6':
                member1=member
                member_id = input("Member ID: ")
                name = input("Member Name: ")
                role = input("Role (admin/user): ")
                member = Member(member_id, name, role)
                library.register_member(member)
                member=member1
                
            elif choice == '7':
                display_all_members(library)
                
            elif choice == '8':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                borrow_book(library, user_id, book_id)

            elif choice == '9':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                return_book(library, user_id, book_id)

            elif choice == '10':
                save_book(library)
                save_member(library)
                
            elif choice == '11':
                save_book(library)
                save_member(library)
                break


        elif member.role == 'user':
            user_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                display_books_menu(library)
            
            elif choice == '2':
                filter_by_genre(library)

            elif choice == '3':
                Search_books(library)
                
            elif choice == '4':
                display_all_books(library)
                book_id = input("Book ID: ")
                borrow_book(library, member.member_id, book_id)

            elif choice == '5':
                if member.borrowed_books:
                    print("Your borrowed books:")
                    for book_id in member.borrowed_books:
                        book = library.books[book_id]
                        print(f"{book.book_id} - {book.title} by {book.author}")
                    book_id = input("Book ID: ")
                    return_book(library, member.member_id, book_id)
                else:
                    print("You have not borrowed any books.")

            elif choice == '6':
                if member.borrowed_books:
                    print("Your borrowed books:")
                    for book_id in member.borrowed_books:
                        book = library.books[book_id]
                        print(f"{book.book_id} - {book.title} by {book.author}")
                else:
                    print("You have not borrowed any books.")
            elif choice == '7':
                save_book(library)
                save_member(library)
            
            elif choice == '8':
                save_book(library)
                save_member(library)
                break   
            
if __name__ == "__main__":
    main()