

from book import Book
from member import Member

# start= input("")

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
            print("\n current selection: Register a member")
            mymember.register_member()
        elif press=="u":
            print("\n current selection: Update a member")
            mymember.update_member()
        elif press=="MI":
            print("\n current selection: Get member info")
            mymember.member_info()
        elif press=="rem":
            print("\n current selection: Remove a member")
            mymember.remove_member()
        elif press=="q":
            break
        else:
            continue
except Exception as e:
    print("There is something wrong, please try again")

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
    print("There is something wrong, please try again")


if __name__ == "__main__":
  main()