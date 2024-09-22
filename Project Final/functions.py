# transaction.py
from book import Book
from member import Member
from data_handler import *


# borrow book from books to member 
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

# Return Book from member to books
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

# delete members and handle if the member borrowed books 
def delete_member(library):
    member_id = input("Enter the ID of the member you want to delete: ")
    
    if member_id in library.members:
        member = library.members[member_id]
        
        # Check if the member has borrowed books
        if member.borrowed_books:
            print(f"Member {member.name} has borrowed the following books:")
            for book_id in member.borrowed_books:
                book = library.books.get(book_id)
                if book:
                    print(f"{book.book_id} - {book.title} by {book.author}")
            
            force_delete = input("Do you want to delete this member and return all borrowed books? (yes/no): ").lower()
            
            if force_delete == "yes":
                for book_id in member.borrowed_books:
                    book = library.books.get(book_id)
                    if book:
                        book.available = True
                        print(f"Returned '{book.title}' by {book.author}.")
                del library.members[member_id]
                print(f"Member with ID {member_id} has been deleted.")
            
            else:
                print("Member deletion canceled.")
        
        else:
            confirm = input(f"Are you sure you want to delete member {member.name}? (yes/no): ").lower()
            
            if confirm == "yes":
                del library.members[member_id]
                print(f"Member with ID {member_id} has been deleted.")
            else:
                print("Member deletion canceled.")
    
    else:
        print(f"No member found with ID {member_id}.")

# register new member 
def new_member(library):
    while True:
        member_id = input("New Member ID: ")
        if not member_id.isdigit():
            print("Invalid Member ID. Please enter a valid numeric ID.")
            continue
        name = input("Member Name: ")
        role = input("Enter the new role (admin/user): ").lower()
        if role not in ['admin', 'user']:
            print("Invalid role.")
            continue
        member = Member(member_id, name, role)
        return member

#update member data 
def update_member(library):
    member_id = input("Enter the ID of the member you want to update: ")
    
    if member_id in library.members:
        member = library.members[member_id]
        print(f"Updating information for {member.name} (ID: {member_id})")
        
        # Ask what the admin wants to update
        update_choice = input("What would you like to update? (1: Name, 2: Role): ")
        
        if update_choice == '1':
            new_name = input("Enter the new name: ")
            member.name = new_name
            print(f"Member's name has been updated to {new_name}.")
        
        elif update_choice == '2':
            new_role = input("Enter the new role (admin/user): ").lower()
            if new_role in ['admin', 'user']:
                member.role = new_role
                print(f"Member's role has been updated to {new_role}.")
            else:
                print("Invalid role. Role not updated.")
        else:
            print("Invalid choice. Nothing was updated.")
    else:
        print(f"No member found with ID {member_id}.")

def admin_menu(name):
    print(f"\n--- Menu for {name} ---")
    print("1. Register a Member")
    print("2. Delete a Member")
    print("3. Update a Member")
    print("4. View All Members")
    print("5. Add a Book")
    print("6. Remove a Book")
    print("7. Display Books")
    print("8. Filter by Genre")
    print("9. Search Books")
    print("10. Borrow a Book for users")
    print("11. Return a Book for users")
    print("12. Save")
    print("13. Save and Exit")

def user_menu(name):
    print(f"\n--- Menu for {name}---")
    print("1. Display Books")
    print("2. Filter by Genre")
    print("3. Search Books")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. View Borrowed Books")
    print("7. Save")
    print("8. Save and Exit")
    
#use this function if using the app for the first time to create the first admin 
def create_first_admin(library):
    if len(library.members) == 0:
        while True:
            print("No members found. Creating an admin account.")
            member_id = input("Enter Admin ID: ")
            if not member_id.isdigit():
                print("Invalid Member ID. Please enter a valid numeric ID.")
                continue  
            member_name = input("Enter Admin Name: ")
            admin = Member(member_id, member_name, role='admin')
            library.register_member(admin)
            save_member(library)
            print("Admin account created successfully!")
            return admin
    return None

# display all books in table format
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

# display all members in table format
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


#Menu for display option (all books , available books)
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


# function to filter books by genre 
def filter_by_genre(library):
    # Get all unique genres in the library
    while True:
        genres = {book.genre for book in library.books.values()}
        genres = sorted(genres)  

        if not genres:
            print("No genres available in the library.")
            break
        
        
        print("\n--- Select a Genre to Filter By ---")
        for idx, genre in enumerate(genres, 1):
            print(f"{idx}. {genre}")
        print(f"{len(genres)+1}. Back to Main Menu")
        
        try:
            genre_choice = int(input("Enter the number of the genre you want to view: "))
            if 1 <= genre_choice <= len(genres):
                selected_genre = genres[genre_choice - 1]
                
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



# Function to search books by title or author or genre 
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
