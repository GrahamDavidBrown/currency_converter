import Currency
rates = {"$": 1.00, "¥": 120.00, "†": .07}

class UnknownCurrencyCodeError(ValueError):
    pass

class Currency_converter:
    def __init__(self, currency, new_currency_code, rates):
        if new_currency_code not in rates:
            raise UnkownCurrencyCodeError("Unknown monetary unit")
        else:
            return currency.multiply(rates[new_currency_code])
