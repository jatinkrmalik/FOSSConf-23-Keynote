
class p: # Product
    def __init__(i, n, pr):
        i.n = n  # name
        i.pr = pr # price

class o: # Order
    def __init__(i, p, q, t, s):
        i.p = p  # price
        i.q = q  # quantity
        i.t = t  # tax rate
        i.s = s  # shipping cost

    def calc(i):
        c = i.p.pr * i.q # total cost
        c += c * i.t
        c += i.s
        return c

def util_calc(p, q, t, s): 
    return p.pr * q + p.pr * q * t + s


def test():
    prod = p("Widget", 20.0)  
    ord = o(prod, 3, 0.05, 5.0) 
    assert ord.calc() == 60.0, "Calculation error"
    assert util_calc(prod, 5, 0.05, 5.0) == 70.0, "Utility calculation error"
    print("All tests passed!") # We should log these messages? 

test()
