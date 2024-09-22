from book import Book
from member import Member
from library import Library

# save books data to books_data.txt 
def save_book(library):
    with open('books_data.txt', 'w') as book_file:
        for book in library.books.values():
            book_file.write(f"{book.book_id},{book.title},{book.author},{book.genre},{book.available}\n")

    print("Books data saved successfully.")

# save members data to members_data.txt 
def save_member(library):
    with open('members_data.txt', 'w') as member_file:
        for member in library.members.values():
            borrowed_books_str = ",".join(member.borrowed_books) 
            member_file.write(f"{member.member_id},{member.name},{member.role},{borrowed_books_str}\n")

    print("Members data saved successfully.")

# Read data from text files and save it in the library 
def load_data():
    library = Library()
    try:
        # Load books data from text file
        with open('books_data.txt', 'r') as book_file:
            for line in book_file:
                book_data = line.strip().split(',')  
                book_id, title, author, genre, available = book_data
                available = available == 'True'  
                book = Book(book_id, title, author, genre, available)
                library.books[book_id] = book
        print("Books data loaded successfully.")
        
        
        # Load members data from text file
        with open('members_data.txt', 'r') as member_file:
            for line in member_file:
                member_data = line.strip().split(',') 
                member_id = member_data[0]
                name = member_data[1]
                role = member_data[2]
                borrowed_books = member_data[3:]  
                member = Member(member_id, name, role, borrowed_books)
                library.members[member_id] = member
        print("Member data loaded successfully.")
        return library
    except FileNotFoundError:
        print("No previous data found.")
        return library