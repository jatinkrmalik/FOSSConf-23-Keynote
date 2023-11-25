# Class for books
class b:
    def __init__(i, t, a, y):
        i.t = t  # title
        i.a = a  # author
        i.y = y  # year

# Class for managing books
class m:
    def __init__(i, bks):
        i.bks = bks  # list of books

    # Check if a book is old
    def chk_old(i):
        old = []
        for b in i.bks:
            if b.y < 2000:  # Check if year is less than 2000
                old.append(b)
        return old

# Utility function
def util(x, y):
    # Complex logic, DO NOT TOUCH!
    return (x * 2) > 10 and (y - 3) < 10

# Test function
def test():
    book = b("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    lib = m([book])
    assert len(lib.chk_old()) == 1  # Check if the book is old
    assert util(6, 14) == False  # Test utility function
    print("Tests passed")

test()
