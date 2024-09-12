from book import Book
from member import Member

def save_book(book):
    with open('list_of_books.txt', 'w') as bk:
        for book in book.books_dec.values():
           bk.write(f"{book.bid},{book.books_title},{book.status}\n")
    print("Data of books saved successfully to text files.")

def save_member(member):
    with open('list_of_members.txt', 'w') as mem:
        for member in member.members_dec.values():
            borrowed_books_str = ",".join(member. borrowed_books) 
            mem.write(f"{member.member_id},{member.name},{borrowed_books_str}\n")

    print("Data of members saved successfully to text files.")

def load_data():
    member = Member("list_of_members.txt","python's library")
    book = Book("list_of_books.txt","python's library")
    
    try:
        with open('list_of_books.txt', 'r') as bk:
            for line in bk:
                book_data = line.strip().split(',')  
                bid= book_data[0]
                books_title= book_data[1]
                status = book_data[2]
                available = available == 'True'  
                book = Book(bid, books_title, status)
                book.books[bid] = book

        with open('list_of_members.txt', 'r') as mem:
            for line in mem:
                member_data = line.strip().split(',')  
                member_id = member_data[0]
                name = member_data[1]
                borrowed_books = member_data[3:] 
                member = Member(member_id, name, borrowed_books)
                member.members[member_id] = member

        print("Library data loaded successfully from text files.")
        return member,book

    except FileNotFoundError:
        print("No previous data found.")
        return Member("list_of_members.txt","python's library"), Book("list_of_books.txt","python's library")
