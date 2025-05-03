class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=True
        print(f"Book created: '{self.title}' by {self.author}")
        
    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, {self.title} is already borrowed")
        else:
            print(f"You have borrowed '{self.title}'.")
            
            
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Thank you for returning '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed out.")
    
    def __str__(self):
        print("Book Details:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        status = 'Borrowed' if self.is_borrowed else 'available'
        print(f"Status: {status}")
        
        
    # def display(self):
        
        

        



class library:
    def __init__(self):
        self.books = []
        print("Library created")
    
    def addBooks(self,book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"The {book} is added to the library.")
        else:
            print("Error! Can only add Book object to the library")
    
    def list_available_books(self):
        print("---Available Books---")
        available_count = 0
        for book in self.books:
            if not book.is_borrowed: