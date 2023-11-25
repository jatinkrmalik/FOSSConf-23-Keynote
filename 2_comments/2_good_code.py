OLD_BOOK_YEAR_THRESHOLD = 2000
DISCOUNT_QUANTITY_THRESHOLD = 5
DISCOUNT_PRICE_THRESHOLD = 10

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library:
    def __init__(self, books):
        self.books = books

    def find_old_books(self):
        return [book for book in self.books if book.publication_year < OLD_BOOK_YEAR_THRESHOLD]

def is_eligible_for_discount(quantity, price):
    quantity_condition = (quantity * 2) > DISCOUNT_QUANTITY_THRESHOLD
    price_condition = (price - 3) < DISCOUNT_PRICE_THRESHOLD
    return quantity_condition and price_condition

def test_library_system():
    great_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library = Library([great_gatsby])
    assert len(library.find_old_books()) == 1, "Should identify old books correctly"
    assert is_eligible_for_discount(6, 14) == False, "Discount eligibility should be calculated correctly"
    print("All tests passed")

test_library_system()
