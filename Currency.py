class DifferentCurrencyCodeError(ValueError):
    pass


class CurrencyCodeError(TypeError):
    pass


class Currency:
    def __init__(self, country_code, amount=0):
        found_cc = False
        try:
            int(country_code[0])
        except ValueError:
            input_country_code = country_code[0]
            country_code = country_code[1:]
            found_cc = True
        try:
            int(country_code[-1])
        except ValueError:
            if not found_cc:
                input_country_code = country_code[-1]
                country_code = country_code[:-1]
        self.country_code = input_country_code
        self.amount = float(country_code)
        if self.country_code == "":
            self.country_code = input("Please enter a currency symbol: ")
        if self.amount == 0:
            self.amount = int(input("Please enter a positive nonzero number: "))
        print(self.amount)
        print(self.country_code)

    def __eq__(self, other):
        if self.country_code == other.country_code and self.amount == other.amount:
            return True
        else:
            return False

    def subtract(self, other):
        if self.contry_code == other.contry_code:
            self.amount -= other.amount
            return (self)
        else:
            raise DifferentCurrencyCodeError("Cannot perform addition on different currencies.")

    def add(self, other):
        if self.contry_code == other.contry_code:
            self.amount += other.amount
            return (self)
        else:
            raise DifferentCurrencyCodeError("Cannot perform subtraction on different currencies.")

    def multiply(self, other):
        if type(other) == int or type(other) == float:
            self.amount = self.amount * other
            return (self)
        else:
            raise CurrencyCodeError("Cannot perform multiplication on currency and currency.")
