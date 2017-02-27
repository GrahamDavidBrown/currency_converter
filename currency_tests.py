from Currency import Currency

c = Currency("$", 5)
d = c
e = Currency("#", 5)
f = Currency("$", 10)
g = Currency("#", 10)

# (c == d), (c != e), (c != f), (c != g)


def test_is_equal(c, d):
    assert (c == d) == True

def test_code_is_not_equal(c, f):
    assert (c == e) == False

def test_amount_is_not_equal(c, f):
    assert (c == f) == False

def test_neither_is_equal(c, g):
    assert (c == g) == False


test_is_equal(c, d)
