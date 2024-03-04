import sys

print("#"*150)
print("Library Manager".center(150))
print("#"*150)
#Initialize the variable to store the data
books_list = []
author_set = set()
books_dict = {}

books_list.append("Python Programming")
author_set.add("John Smmith")
books_dict["Python Programming"] = "John Smmith"

books_list.append("Data structure and Algorithm")
author_set.add("John Doe")
books_dict["Data structure and Algorithm"] = "John Doe"

books_list.append("Machine Leaening Basics")
author_set.add("Alicce Jonhson")
books_dict["Machine Leaening Basics"] = "Alicce Jonhson"



#Search for the book

def search_book():
    search_title = input ("Enter the title of the book: ")
    if search_title in books_list:
        print (f"Book found! \n Author: {books_dict[search_title]}")
    else:
        print("Book not found")

#Dispay the book
def show_book_list():
    print ("List of books: ")
    for book in books_list:
        print (book)

#Remove the books
def remove_book():
    remove_title = input("Enter the titble of book to remove: ")
    if remove_title in books_list:
        remove_author = books_dict[remove_title]
        books_list.remove(remove_title)
        author_set.remove(remove_author)
        del books_dict[remove_title]

        print ("Book removed successfully!")
        print("Books Available: \n", books_list)

    else:
        print("Book not found!")

def add_book():
    pass


while True:
    user_action = input("""
Press 1 to see booklist
Press 2 to search books
Press 3 to add books
Press 4 to remove book
Press Q to exit
>>> """)
    print()
    
    if user_action == "1":
        show_book_list()
    elif user_action == "2":
        search_book()
    elif user_action == "3":
        add_book()
    elif user_action == "4":
        remove_book()
    elif user_action == "Q".lower():
        print("#"*150)
        print ("The Program exits. Have a good day ahead.".center(150))
        print("#"*150)
        sys.exit()
    else:
        print("Invalid input")
         

