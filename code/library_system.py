# Smart Library Management System
# COM5012 OOP Coursework

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")


# Inheritance: BorrowableBook inherits from Book
class BorrowableBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.due_date = None

    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            self.due_date = "7 days"
            print(f"{self.title} has been borrowed.")
        else:
            print("Book is not available.")

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            self.due_date = None
            print(f"{self.title} has been returned.")
        else:
            print("Book was not borrowed.")

    # Polymorphism (method override)
    def display_info(self):
        super().display_info()
        if self.due_date:
            print(f"Due Date: {self.due_date}")


class Member:
    def __init__(self, member_id):
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 5:
            print("Borrowing limit reached.")
        elif book.status == "Available":
            book.borrow_book()
            self.borrowed_books.append(book)
        else:
            print("Book not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the member.")


# Main Program
def main():

    book1 = BorrowableBook("Python Basics", "John Smith")
    book2 = BorrowableBook("Data Science 101", "Jane Doe")

    member = Member("M001")

    while True:
        print("\nLibrary System")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book1.display_info()
            print()
            book2.display_info()

        elif choice == "2":
            member.borrow_book(book1)

        elif choice == "3":
            member.return_book(book1)

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")


main()
