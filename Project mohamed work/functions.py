# transaction.py
from book import Book
from member import Member
from data_handler import *

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


def admin_menu():
    print("\n--- Admin Menu ---")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Display Books")
    print("4. Filter by Genre")
    print("5. Search Books")
    print("6. Register a Member")
    print("7. View All Members")
    print("8. Borrow a Book for users")
    print("9. Return a Book for users")
    print("10. Save")
    print("11. Save and Exit")

def user_menu():
    print("\n--- User Menu ---")
    print("1. Display Books")
    print("2. Filter by Genre")
    print("3. Search Books")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. View Borrowed Books")
    print("7. Save")
    print("8. Save and Exit")
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



def display_books_menu(library):
    while True:
        print("\n--- Display Books Menu ---")
        print("1. Display All Books")
        print("2. Display Available Books")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_all_books(library)  # Display all books
        elif choice == '2':
            display_available_books(library)  # Display only available books
        elif choice == '3':
            break  # Go back to main menu
        else:
            print("Invalid choice. Please enter a valid option.")


# Function to display all books

# Function to display only available books
def display_available_books(library):
    available_books = [book for book in library.books.values() if book.available]
    if available_books:
        print("\n--------------------------------------------------- Available Books ---------------------------------------------------")
        print(f"{'ID'.ljust(5)} {'Title'.ljust(35)} {'Author'.ljust(30)} {'Genre'.ljust(30)} {'Status'.ljust(10)}")
        print("-" * 113)
        for book in available_books:
            status = "Available"
            print(f"{book.book_id.ljust(5)} {book.title.ljust(35)} {book.author.ljust(30)} {book.genre.ljust(30)} {status.ljust(10)}")
    else:
        print("No available books.")



def filter_by_genre(library):
    # Get all unique genres in the library
    while True:
        genres = {book.genre for book in library.books.values()}
        genres = sorted(genres)  # Sort genres for easier navigation

        if not genres:
            print("No genres available in the library.")
            break
        
        # Display all genres with a corresponding number for selection
        print("\n--- Select a Genre to Filter By ---")
        for idx, genre in enumerate(genres, 1):
            print(f"{idx}. {genre}")
        print(f"{len(genres)+1}. Back to Main Menu")
        try:
            # Ask user to select a genre
            genre_choice = int(input("Enter the number of the genre you want to view: "))
            if 1 <= genre_choice <= len(genres):
                selected_genre = genres[genre_choice - 1]
                # Filter and display books with the selected genre
                filtered_books = [book for book in library.books.values() if book.genre == selected_genre]
                
                if filtered_books:
                    print(f"\n--------------------------------------------------- {selected_genre} Books ---------------------------------------------------")
                    print(f"{'ID'.ljust(5)} {'Title'.ljust(35)} {'Author'.ljust(30)} {'Genre'.ljust(30)} {'Status'.ljust(10)}")
                    print("-" * 113)
                    for book in filtered_books:
                        status = "Available" if book.available else "Checked Out"
                        print(f"{book.book_id.ljust(5)} {book.title.ljust(35)} {book.author.ljust(30)} {book.genre.ljust(30)} {status.ljust(10)}")
                else:
                    print(f"No books found in genre '{selected_genre}'.")
            elif genre_choice == len(genres)+1:
                break
            else:
                print("Invalid genre selection.")
        except ValueError:
            print("Please enter a valid number.")



# Function to search books by title or author or genre or title
def Search_books(library):
    while True:
    
        print("\n--- Search Books Menu ---")
        print("1. Search Books by Title")
        print("2. Search Books by Author")
        print("3. Search Books by Genre")
        print("4. Back to Main Menu")
        search_option = input("Enter your choice: ")
        
        # Search by Title
        if search_option == '1':
            title = input("Enter the title name to search by: ").strip()
            searched_books = [book for book in library.books.values() if title.lower() in book.title.lower()]
            if searched_books:
                print(f"\n--------------------------------------------------- Books by Title: {title} ---------------------------------------------------")
                print(f"{'ID'.ljust(5)} {'Title'.ljust(35)} {'Author'.ljust(30)} {'Genre'.ljust(30)} {'Status'.ljust(10)}")
                print("-" * 113)
                for book in searched_books:
                    status = "Available" if book.available else "Checked Out"
                    print(f"{book.book_id.ljust(5)} {book.title.ljust(35)} {book.author.ljust(30)} {book.genre.ljust(30)} {status.ljust(10)}")
            else:
                print(f"No books found by title '{title}'.")
                
        # Search by Author        
        elif search_option == '2':
            author = input("Enter the author name to search by: ").strip()
            searched_books = [book for book in library.books.values() if author.lower() in book.author.lower()]
            if searched_books:
                print(f"\n--------------------------------------------------- Books by Author: {author} ---------------------------------------------------")
                print(f"{'ID'.ljust(5)} {'Title'.ljust(35)} {'Author'.ljust(30)} {'Genre'.ljust(30)} {'Status'.ljust(10)}")
                print("-" * 113)
                for book in searched_books:
                    status = "Available" if book.available else "Checked Out"
                    print(f"{book.book_id.ljust(5)} {book.title.ljust(35)} {book.author.ljust(30)} {book.genre.ljust(30)} {status.ljust(10)}")
            else:
                print(f"No books found by author '{author}'.")
        
        # Search by Genre
        elif search_option == '3':
            genre = input("Enter the genre to filter by: ").strip()
            searched_books = [book for book in library.books.values() if genre.lower() in book.genre.lower()]
            
            if searched_books:
                print(f"\n--------------------------------------------------- Books by Genre: {genre} ---------------------------------------------------")
                print(f"{'ID'.ljust(5)} {'Title'.ljust(35)} {'Author'.ljust(30)} {'Genre'.ljust(30)} {'Status'.ljust(10)}")
                print("-" * 113)
                for book in searched_books:
                    status = "Available" if book.available else "Checked Out"
                    print(f"{book.book_id.ljust(5)} {book.title.ljust(35)} {book.author.ljust(30)} {book.genre.ljust(30)} {status.ljust(10)}")
            else:
                print(f"No books found in genre '{genre}'.")
        elif search_option == '4':
            break
        else:
            print("Invalid option. Please enter valid number.")
