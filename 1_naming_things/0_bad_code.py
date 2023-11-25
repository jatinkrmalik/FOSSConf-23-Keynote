class p:
    def __init__(i, n, pr):
        i.n = n
        i.pr = pr

class o:
    def __init__(i, p, q, t, s):
        i.p = p
        i.q = q
        i.t = t
        i.s = s

    def calc(i):
        c = i.p.pr * i.q
        c += c * i.t
        c += i.s
        return c

def util_calc(p, q, t, s):
    return p.pr * q + p.pr * q * t + s

def test():
    prod = p("Widget", 20.0)
    ord = o(prod, 3, 0.05, 5.0)
    assert ord.calc() == 60.0, "err"
    assert util_calc(prod, 5, 0.05, 5.0) == 70.0, "err"
    print("Pass!")

test()
