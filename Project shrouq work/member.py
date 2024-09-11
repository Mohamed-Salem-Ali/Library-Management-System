class Member:
    """This class is used to register, update, remove, and Track member information, including borrowed books """
    def __init__(self, list_of_members,library_name):
     self.list_of_members = list_of_members
     self.library_name = library_name
     self.members_dec = {}
     ID = 100
     list_of_members = r"C:\Users\2A\mylibrary\Library-Management-System\Project shrouq work\list_of_members.txt"
     with open(self.list_of_members) as mem:
        names= mem.readlines()
     for line in names:
        self.members_dec.update({str(ID):{"member_name":line.replace("\n",""),"borrowed_books":""}})
        ID+=1

    def register_member(self, member_id, name):
        member_id= input("Enter your ID: ")
        name= input("Enter your Name: ")
        if member_id in self.members_dec:
            print(f"Member with ID {member_id} already exists.")
        else:
            self.members_dec[member_id] = {'name': name, 'borrowed_books': []}
            print(f"Member {name} with ID {member_id} registered successfully.")
            
    def update_member(self, member_id, name=None, borrowed_books=None):
        member_id= input("Enter your ID: ")
        borrowed_books= input("What books did you borrow? ")
        
        if member_id not in self.members_dec:
            print(f"No member found with ID {member_id}.")
        else:
            if name:
                self.members_dec[member_id]['name'] = name
                print(f"Member name updated to {name}.")
            if borrowed_books is not None:
                self.members_dec[member_id]['borrowed_books'] = borrowed_books
                print(f"Borrowing history updated for member ID {member_id}.")
                
    def remove_member(self, member_id):
        member_id= input("Enter your ID: ")
        if member_id in self.members_dec:
            del self.members_dec[member_id]
            print(f"Member with ID {member_id} removed successfully.")
        else:
            print(f"No member found with ID {member_id}.")
            
    def member_info(self, member_id):
        member_id= input("Enter your ID: ")
        return self.members_dec.get(member_id, None)