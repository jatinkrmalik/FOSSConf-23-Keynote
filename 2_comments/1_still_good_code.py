# Constants used to replace magic numbers
OLD_BOOK_YEAR_THRESHOLD = 2000
DISCOUNT_QUANTITY_THRESHOLD = 5
DISCOUNT_PRICE_THRESHOLD = 10

class Book:
    # Using descriptive variable names instead of abbreviations
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library:
    # Clear class and variable names for better understanding
    def __init__(self, books):
        self.books = books

    def find_old_books(self):
        # List comprehension for concise and readable code
        return [book for book in self.books if book.publication_year < OLD_BOOK_YEAR_THRESHOLD]

# Function extraction for complex logic
def is_eligible_for_discount(quantity, price):
    # Breaking down complex condition for readability
    quantity_condition = (quantity * 2) > DISCOUNT_QUANTITY_THRESHOLD
    price_condition = (price - 3) < DISCOUNT_PRICE_THRESHOLD
    return quantity_condition and price_condition

def test_library_system():
    # Creating instances with clear and descriptive names
    great_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library = Library([great_gatsby])
    # Assert statements with clear, descriptive error messages
    assert len(library.find_old_books()) == 1, "Should identify old books correctly"
    assert is_eligible_for_discount(6, 14) == False, "Discount eligibility should be calculated correctly"
    # Using print for simple output, could be replaced with logging for more complex applications
    print("All tests passed")

test_library_system()
