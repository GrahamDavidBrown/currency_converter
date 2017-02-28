class DifferentCurrencyCodeError(ValueError):
    pass


class CurrencyCodeError(TypeError):
    pass


class Currency:
    def __init__(self, country_code, amount=0):
        if len(country_code) == 1:
            self.amount = amount
            self.country_code = country_code
        else:
            try:
                int(country_code[0])
            except ValueError:
                self.country_code = country_code[:1]
                country_code = country_code[1:]
            try:
                int(country_code[-1])
            except ValueError:
                self.country_code = country_code[-1:]
                country_code = country_code[:-1]
            try:
                self.amount = float(country_code)
            except ValueError:
                print("your input obviously makes no sense.")


    def __eq__(self, other):
        if (self.country_code == other.country_code) and (self.amount == other.amount):
            return True
        else:
            return False

    def subtract(self, other):
        if self.contry_code == other.contry_code:
            (self.amount) -= (other.amount)
            return (self)
        else:
            raise DifferentCurrencyCodeError("Cannot perform addition on different currencies.")

    def add(self, other):
        if self.country_code == other.country_code:
            (self.amount) += (other.amount)
            return (self)
        else:
            raise DifferentCurrencyCodeError("Cannot perform subtraction on different currencies.")

    def multiply(self, other):
        if type(other) == int or type(other) == float:
            self.amount = self.amount * other
            return (self)
        else:
            raise CurrencyCodeError("Cannot perform multiplication on currency and currency.")
