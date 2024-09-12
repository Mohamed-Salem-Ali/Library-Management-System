
from book import Book
from member import Member
from data_handler import save_book, save_member, load_data


def create_first_admin(member):
    if len(member.members) == 0:
        print("No members found. Creating an admin account.")
        admin_id = input("Enter Admin ID: ")
        admin_name = input("Enter Admin Name: ")
        admin = Member(admin_id, admin_name,)
        member.register_member(admin)
        save_member(member)
        print("Admin account created successfully!")
        return admin
    return None

def main():
   member= load_data() 
   book = load_data() 

memberrole= input("Are you admin or user? ")

if memberrole== 'admin':
        try:
            mymember= Member("list_of_members.txt","python's library")
            presskeys= {"R": "Register a member","U":"Update a member", "MI": "Get member info", "Rem":"Remove a member","Q":"quit"}
            press= False
            while not(press=="q"):
                print(f"\n","-"*10,"Welcomne to our Library", "-"*10)
                for key,value in presskeys.items():
                    print("press", key, "To",value)
                press= input ("press key: ").lower()
                if press =="r":
                    print("\n current selection: Register as an admin")
                    mymember.register_member(0,"")
                elif press=="u":
                    print("\n current selection: Update a member")
                    mymember.update_member(0)
                elif press=="MI":
                    print("\n current selection: Get member info")
                    mymember.member_info(0)
                elif press=="rem":
                    print("\n current selection: Remove a member")
                    mymember.remove_member(0)
                elif press=="q":
                    break
                else:
                    continue
        except Exception as e:
            print("There is something wrong, please try again",e)

elif memberrole == 'user':
        try:
            mybook= Book("list_of_books.txt","python's library")
            presskeys= {"D": "display books","I":"issue (borrow) book", "A": "add book", "R":"return book", "DEL":"Delete book","Q":"quit"}
            press= False
        
            while not(press=="q"):
                print(f"\n","-"*10,"Welcomne to our Library", "-"*10)
                for key,value in presskeys.items():
                    print("press", key, "To",value)
                press= input ("press key: ").lower()
                if press =="d":
                    print("\n current selection:display books")
                    mybook.display_books()
                elif press=="i":
                    print("\n current selection: issue (borrow) book")
                    mybook.issue_books()
                elif press=="r":
                    print("\n current selection: return book")
                    mybook.return_books()
                elif press=="a":
                    print("\n current selection: add book")
                    mybook.add_books()
                elif press== "del":
                    print("\n current selection: delete book")
                    mybook.delete_book()
                elif press=="q":
                    break
                else:
                    continue
        except Exception as e:
            print("There is something wrong, please try again",e) 
if __name__ == "__main__":
    main()
    
     
# try:
#     mybook= Book("list_of_books.txt","python's library")
#     presskeys= {"D": "display books","I":"issue (borrow) book", "A": "add book", "R":"return book", "DEL":"Delete book","Q":"quit"}
#     press= False
    
#     while not(press=="q"):
#         print(f"\n","-"*10,"Welcomne to our Library", "-"*10)
#         for key,value in presskeys.items():
#             print("press", key, "To",value)
#         press= input ("press key: ").lower()
#         if press =="d":
#             print("\n current selection:display books")
#             mybook.display_books()
#         elif press=="i":
#             print("\n current selection: issue (borrow) book")
#             mybook.issue_books()
#         elif press=="r":
#             print("\n current selection: return book")
#             mybook.return_books()
#         elif press=="a":
#             print("\n current selection: add book")
#             mybook.add_books()
#         elif press== "del":
#             print("\n current selection: delete book")
#             mybook.delete_book()
#         elif press=="q":
#             break
#         else:
#             continue
# except Exception as e:
#     print("There is something wrong, please try again")
