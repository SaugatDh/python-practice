class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed = False
    
    def borrow_book(self):
        if self.is_borrowed is True:
            print(f"{self.title} by {self.author} is already borrowed.")
        else:
            print(f"You borrowed {self.title} by {self.author}")
            self.is_borrowed=True
    def return_book(self):
        if self.is_borrowed is True:
            print(f"Thank you for returning {self.title}")
            self.is_borrowed=False
        else:
            print("You cant return the book that you dont have borrowed.")
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def display(self):
        print(self)
        if self.is_borrowed is True:
            print("Status: Not Available.")
        else:
            print("Status: Available.")

class Library:
    def __init__(self,books=[]):
        self.books=books
        
    def add_books(self,book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title} by {book.author}")
        else:
            print("Error")
    
    def available_books(self):
        available = False
        print("########## Available Books to borrow. ##########")
        for book in self.books:
            if not book.is_borrowed:
                book.display()
                available = True
        if not available:
            print("No available books.")
        print("########## ##########")

    def all_books(self):
        print("------------All books: ------------")
        for book in self.books:
            book.display()
        print("-----------------------------------")
        
            
        



book1 = Book("Harry Potter","JK Rowling")
book2 = Book("Cheena harayeko mancche","Hari Bangsha Acharya")
# book1.borrow_book()
# book1.return_book()
# book1.borrow_book()
book2.borrow_book()


myLibrary = Library([])
myLibrary.add_books(book1)
myLibrary.add_books(book2)
myLibrary.available_books()


