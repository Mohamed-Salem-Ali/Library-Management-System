import datetime

class Book:
    """This class is used to manage books library. It can Add, update, remove, and Track book details (ID, title, author, genre, and availability) """
    def __init__(self, list_of_books,library_name):
     self.list_of_books = list_of_books
     self.library_name = library_name
     self.books_dec = {}
     ID = 100
     list_of_books = r"C:\Users\2A\mylibrary\Library-Management-System\Project shrouq work\list_of_books.txt"
     with open(self.list_of_books) as bk:
        names= bk.readlines()
     for line in names:
        self.books_dec.update({str(ID):{"books_title":line.replace("\n",""),
                          "lender_name":"", "status":"Avaliable"}})
        ID+=1
        
    def display_books(self):
        print("-"*10, "list of books", "-"*10)
        print("book's ID","\t","title")
        print("-"*30)
        for key, value in self.books_dec.items():
            print(key,"\t\t", value.get("books_title"), "-[",value.get("status"),"]")
 
    def issue_books(self):
        bid= input("enter book's ID: ")
        current_date=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if bid in self.books_dec.keys():
            if self.books_dec[bid]["status"]=="Avaliable":
             yname=input("Enter your name: ")
             self.books_dec[bid]["lender_name"]= yname
             self.books_dec[bid]["issue_date"]= current_date
             print("Book is borrowed succesfully \n")
             self.books_dec[bid]["status"]= "Alread borrowed"
            
            elif self.books_dec[bid]["status"]=="Alread borrowed":
              print(f"This book is already borrowed to {self.books_dec[bid]['lender_name']} on {current_date}")
              return self.issue_books()         
        else:
            print("Book is is not found, please enter a correct ID")
    
    def delete_book(self):
        delbook= input("Enter the id of book to delete: ")
        del self.books_dec[delbook]
        print("The book has been deleted successfully")
        
           
    def add_books(self):
        new_book=input("Add new book: ")
        if new_book =="":
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dec.update ({str(int(max(self.book_dec))+1):{'books_title': new_book,'lender_name':"",'issue_date':"", 'status': "Avaliable"}})
                print("The new book has been added successfully")

    def return_books(self):
        bid =input("Enter book's ID: ")
        if bid in self.books_dec.keys():
            if self.books_dec[bid]["status"]=="Avaliable":
                print("This book is already avaliable in the library")
                return self.return_books()
            elif not self.books_dec[bid]["status"]=="Avaliable":
                self.books_dec[bid]["lender_name"]= ""
                self.books_dec[bid]["issue_name"]= ""
                self.books_dec[bid]["status"]= "Avaliable"
                print("Successfully updated \n")
        else:
            print("Book is is not found, please enter a correct ID")
        
    
