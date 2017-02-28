from Currency import Currency

c = Currency("$", 5)
d = c
e = Currency("#", 5)
f = Currency("$", 10)
g = Currency("#", 10)
h = 2

# (c == d), (c != e), (c != f), (c != g)


def test_is_equal(c, d):
    assert (c == d) == True

def test_code_is_not_equal(c, e):
    assert (c == e) == False

def test_amount_is_not_equal(c, f):
    assert (c == f) == False

def test_neither_is_equal(c, g):
    assert (c == g) == False

def test_multiply_currencies(c, h):
    assert (c.multiply(h)) == 10

def test_multiply_currencies(c, h):
    assert (c.multiply(h)) == DifferentCurrencyCodeError


test_is_equal(c, d)
test_code_is_not_equal(c, e)
test_amount_is_not_equal(c, f)
test_neither_is_equal(c, g)
test_multiply_currencies(c, d)
test_multiply_currencies(c, h)
