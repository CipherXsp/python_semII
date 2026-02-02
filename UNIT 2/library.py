class LibraryBook:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def checkout_book(self):
        if self.available:
            self.available = False
            print(f"'{self.book_name}' has been checked out.")
        else:
            print(f"'{self.book_name}' is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.book_name}' has been returned.")
        else:
            print(f"'{self.book_name}' is already available.")

    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print()


# Example usage
book1 = LibraryBook("1984", "George Orwell")
book2 = LibraryBook("The Alchemist", "Paulo Coelho", False)

book1.display_book()
book2.display_book()

book1.checkout_book()
book2.return_book()

book1.display_book()
book2.display_book()
