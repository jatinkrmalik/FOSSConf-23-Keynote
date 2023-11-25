# Avoid Single Letter Variable Names, Don't Abbreviate Names, Avoid Putting Types in Names
class p:  # Bad practice: Using single letter class name and abbreviating 'product'
    def __init__(i, n, pr):
        i.n = n  # Bad practice: Abbreviating 'name'
        i.pr = pr  # Bad practice: Abbreviating 'price'

# Include Units in Variable Names, Be Cautious with Naming Conventions
class o:  # Bad practice: Single letter class name 'o' for 'order'
    def __init__(i, p, q, t, s):
        i.p = p  # Bad practice: Single letter variable
        i.q = q  # Bad practice: Single letter variable
        i.t = t  # Bad practice: Single letter variable, unclear unit
        i.s = s  # Bad practice: Single letter variable

    def calc(i):
        c = i.p.pr * i.q  # Bad practice: Single letter variable
        c += c * i.t
        c += i.s
        return c

# Rethink Naming if Struggling, Organize Code Logically
def util_calc(p, q, t, s):  # Bad practice: Generic utility function name
    return p.pr * q + p.pr * q * t + s

# Testing with assert
def test():
    prod = p("Widget", 20.0)  # Bad practice: Single letter variable
    ord = o(prod, 3, 0.05, 5.0)  # Bad practice: Single letter variable
    assert ord.calc() == 60.0, "Calculation error"
    assert util_calc(prod, 5, 0.05, 5.0) == 70.0, "Utility calculation error"
    print("All tests passed!") # We should log these messages? 

test()
