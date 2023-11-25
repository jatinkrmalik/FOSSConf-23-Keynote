# Is it really bad though? 

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class OnlineBookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def process_payment(self, book, user):
        print(f"Processing payment for {user} for the book {book.title}")

    def deliver_book(self, book, user):
        print(f"Delivering {book.title} to {user}")

# Usage
store = OnlineBookStore()
book = Book("1984", "George Orwell", 20)
store.add_book(book)
found_books = store.search_book_by_title("1984")
store.process_payment(found_books[0], "Alice")
store.deliver_book(found_books[0], "Alice")
