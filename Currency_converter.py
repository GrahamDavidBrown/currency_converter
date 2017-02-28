from Currency import Currency
rates = {"$": 1.00, "¥": 120.00, "†": .07}

class UnknownCurrencyCodeError(ValueError):
    pass

class Currency_converter:
    def __init__(self, currency, new_currency_code, rates):
        self.currency = currency
        self.new_currency_code = new_currency_code
        self.rates = rates

    def convert(self):
        if new_currency_code not in rates:
            raise UnkownCurrencyCodeError("Unknown monetary unit")
        else:
            self.currency.amount = self.currency.amount * self.rates[new_currency_code]
            self.currency.country_code = self.new_currency_code
            return self.currency
