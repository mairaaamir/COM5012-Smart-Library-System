# Smart Library Management System
# COM5012 Object Oriented Programming Coursework
#
# This program shows the main ideas of Object-Oriented Programming:
# - Encapsulation: data about books and members is stored inside classes
# - Inheritance: BorrowableBook is a type of Book
# - Polymorphism: the display_info() method is changed in BorrowableBook


class Book:
    # This class represents a basic book in the library
    # It stores the title, author and whether the book is available

    def __init__(self, title, author):
        # When a book object is created, we save its title and author
        self.title = title
        self.author = author

        # By default every book starts as available
        self.status = "Available"

    def display_info(self):
        # This function prints information about the book
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")


# BorrowableBook inherits from Book
# This means it automatically gets the title, author and status from Book
class BorrowableBook(Book):

    def __init__(self, title, author):
        # super() runs the Book class constructor
        # so we don't have to repeat that code
        super().__init__(title, author)

        # This will store the due date when a book is borrowed
        self.due_date = None

    def borrow_book(self):
        # This function lets a member borrow the book
        # It first checks if the book is available

        if self.status == "Available":
            self.status = "Borrowed"

            # For simplicity we just say the due date is 7 days
            self.due_date = "7 days"

            print(f"{self.title} has been borrowed.")
        else:
            print("Book is not available.")

    def return_book(self):
        # This function returns the book to the library

        if self.status == "Borrowed":
            self.status = "Available"
            self.due_date = None

            print(f"{self.title} has been returned.")
        else:
            print("Book was not borrowed.")

    # This method overrides the one from the Book class
    # This is an example of polymorphism
    def display_info(self):

        # Call the original display_info() from the Book class
        super().display_info()

        # If the book is borrowed, show the due date
        if self.due_date:
            print(f"Due Date: {self.due_date}")


class Member:
    # This class represents a library member
    # It keeps track of which books they have borrowed

    def __init__(self, member_id):
        self.member_id = member_id

        # This list stores all books the member has borrowed
        self.borrowed_books = []

    def borrow_book(self, book):
        # This function allows the member to borrow a book

        # The system rule says members can only borrow 5 books
        if len(self.borrowed_books) >= 5:
            print("Borrowing limit reached.")

        # If the book is available, borrow it
        elif book.status == "Available":
            book.borrow_book()

            # Add the book to the member's borrowed list
            self.borrowed_books.append(book)
        else:
            print("Book not available.")

    def return_book(self, book):
        # This function returns a borrowed book

        # Check if the member actually borrowed this book
        if book in self.borrowed_books:
            book.return_book()

            # Remove it from the borrowed list
            self.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the member.")


# Main part of the program
# This runs the menu system
def main():

    # Create some example books
    book1 = BorrowableBook("Python Basics", "John Smith")
    book2 = BorrowableBook("Data Science 101", "Jane Doe")

    # Create a library member
    member = Member("M001")

    # This loop keeps the program running until the user exits
    while True:

        print("\nLibrary System")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            # Show details of the books
            book1.display_info()
            print()
            book2.display_info()

        elif choice == "2":
            # Borrow the first book
            member.borrow_book(book1)

        elif choice == "3":
            # Return the first book
            member.return_book(book1)

        elif choice == "4":
            # Stop the program
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")


# Start the program
main()
