def convert(amount, rate):
    return amount * rate

def choose_rate():
    currency = input('Выберите в какую валюту хотите конвертировать гривны? (EUR, USD, PLN): ')
    return currency

def converter():
    amount = float(input('Введите сумму для конвертации: '))
    currency = choose_rate()

    conversion_rates = {'EUR': 0.024, 'USD': 0.026, 'PLN': 0.11}
    if currency in conversion_rates:
        rate = conversion_rates[currency]
        result = convert(amount, rate)
        print(f'Результат: {amount} гривен = {result} {currency}')
    else:
        print('Ошибка. Вы выбрали несуществующую валюту.')
        
converter()