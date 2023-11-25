class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

# Introducing some abstraction for payment
class PaymentProcessor:
    def process_payment(self, book, user):
        print(f"Processing payment for {user} for the book {book.title}")

# Introducing some abstraction for delivery
class DeliveryService:
    def deliver_book(self, book, user):
        print(f"Delivering {book.title} to {user}")

# Usage
store = BookStore()
store.add_book(Book("1984", "George Orwell", 20))
payment_processor = PaymentProcessor()
delivery_service = DeliveryService()

found_books = store.search_book_by_title("1984")
if found_books:
    book = found_books[0]
    payment_processor.process_payment(book, "Alice")
    delivery_service.deliver_book(book, "Alice")
