def convert(amount, rate):
    return amount * rate

def choose_rate():
    currency = input('Выберите в какую валюту хотите конвертировать гривны? (EUR, USD, PLN): ')
    return currency