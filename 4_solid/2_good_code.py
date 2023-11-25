# Single Responsibility Principle
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        return [book for book in self.books if book.title == title]

# Open/Closed Principle
class PaymentProcessor:
    def process_payment(self, book, user):
        raise NotImplementedError

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, book, user):
        print(f"Processing credit card payment for {user} for the book {book.title}")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, book, user):
        print(f"Processing PayPal payment for {user} for the book {book.title}")

# Liskov Substitution Principle
# Interface Segregation Principle
class DeliveryService:
    def deliver(self, book, user):
        raise NotImplementedError

class HomeDelivery(DeliveryService):
    def deliver(self, book, user):
        print(f"Delivering {book.title} to {user}'s home")

class PickUpStationDelivery(DeliveryService):
    def deliver(self, book, user):
        print(f"{user} can pick up {book.title} from the nearest station")

# Dependency Inversion Principle
class OnlineBookStore:
    def __init__(self, repository, payment_processor, delivery_service):
        self.repository = repository
        self.payment_processor = payment_processor
        self.delivery_service = delivery_service

    def purchase_book(self, title, user):
        book = self.repository.find_by_title(title)[0]
        self.payment_processor.process_payment(book, user)
        self.delivery_service.deliver(book, user)

# Usage
repository = BookRepository()
repository.add_book(Book("1984", "George Orwell", 20))
payment_processor = CreditCardPaymentProcessor()
delivery_service = HomeDelivery()

store = OnlineBookStore(repository, payment_processor, delivery_service)
store.purchase_book("1984", "Alice")
