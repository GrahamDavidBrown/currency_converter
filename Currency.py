class DifferentCurrencyCodeError(ValueError):
    pass


class CurrencyCodeError(TypeError):
    pass


class Currency:
    def __init__(self, country_code, amount=0):
        if len(country_code) == 1:
            self.amount = float(amount)
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


    def __repr__(self):
        return str(self.country_code) + self.amount

    def __eq__(self, other):
        if (self.country_code == other.country_code) and (self.amount == other.amount):
            return True
        else:
            return False

    def __sub__(self, other):
        if self.contry_code == other.contry_code:
            return_val = self
            (return_val.amount) -= (other.amount)
            return return_val
        else:
            raise DifferentCurrencyCodeError("Cannot perform addition on different currencies.")

    def __add__(self, other):
        if self.country_code == other.country_code:
            return_val = self
            (return_val.amount) += (other.amount)
            return return_val
        else:
            raise DifferentCurrencyCodeError("Cannot perform subtraction on different currencies.")

    def multiply(self, other):
        if type(other) == int or type(other) == float:
            return_val = self
            return_val.amount = self.amount * other
            return return_val
        else:
            raise CurrencyCodeError("Cannot perform multiplication on currency and currency.")
