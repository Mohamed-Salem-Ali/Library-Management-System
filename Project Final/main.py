from book import Book
from member import Member
from library import Library
from functions import *
from data_handler import *

def main():
    library = load_data()  # Load existing data

    # Check if there are any members, if not create an admin
    member = create_first_admin(library)

    # login
    while True:
        if not member:
            member_id = input("Enter your Member ID: ")
            if not member_id.isdigit():
                print("Invalid Member ID. Please enter a valid numeric ID.")
                continue  # Re-prompt the user for a valid ID
            if member_id in library.members:
                member = library.members.get(member_id)
                print(f"\nWelcome {member.name}  ^_^")
                break
            else:
                print(f"No member found with ID {member_id}. Please try again.")
                continue
        else:
            print(f"Welcome {member.name}!")
            break
    while True:
        # Check role and display the menu
        
        if member.role == 'admin':
            admin_menu(member.name)
            choice = input("Enter your choice: ")

            if choice == '1':
                display_all_members(library)
                member1=member
                member = new_member(library)
                library.register_member(member)
                member=member1
            
            elif choice == '2':
                display_all_members(library)
                delete_member(library)
                
            elif choice == '3':
                display_all_members(library)
                update_member(library)
                
            elif choice == '4':
                display_all_members(library)
            
            elif choice == '5':
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                genre = input("Genre: ")
                book = Book(book_id, title, author, genre)
                library.add_book(book)
                display_all_books(library)
                
            elif choice == '6':
                display_all_books(library)
                book_id = input("Enter Book ID to remove: ")
                library.remove_book(book_id)
                
            elif choice == '7':
                display_books_menu(library)

            elif choice == '8':
                filter_by_genre(library)

            elif choice == '9':
                Search_books(library)
                
                
            elif choice == '10':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                borrow_book(library, user_id, book_id)

            elif choice == '11':
                user_id = input("User's Member ID: ")
                book_id = input("Book ID: ")
                return_book(library, user_id, book_id)

            elif choice == '12':
                save_book(library)
                save_member(library)
                
            elif choice == '13':
                save_book(library)
                save_member(library)
                break


        elif member.role == 'user':
            user_menu(member.name)
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