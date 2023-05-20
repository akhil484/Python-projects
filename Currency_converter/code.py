from currency_converter import CurrencyConverter

c = CurrencyConverter()
print(c.convert(1, 'USD', 'INR'))

#print all available currencies
print(c.currencies)