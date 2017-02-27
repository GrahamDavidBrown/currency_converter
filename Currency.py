class Currency:
    def __init__(self, country_code, amount):
        self.country_code = country_code
        self.amount = amount

    def __eq__(self, other):
        if self.country_code == other.country_code and self.amount == other.amount:
            return True
        else:
            return False

    def __add__(self, other):
        if self.eq(other):
            return (self.amount + other.amount)
        else:
            raise ValueError
