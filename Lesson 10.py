import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url)
        self.soup = BeautifulSoup(self.data.content, 'html.parser')

    def convert(self, from_currency, to_currency, amount):
        # получаем курс валют
        rates = self.get_rates()
        # проверяем, что выбранные валюты существуют в списке курсов
        if from_currency not in rates or to_currency not in rates:
            return "Ошибка: валюты не найдены в списке курсов."
        # конвертируем из from_currency в to_currency
        converted_amount = amount * (rates[to_currency] / rates[from_currency])
        return converted_amount

    def get_rates(self):
        # находим таблицу с курсами валют и извлекаем информацию о курсах
        currency_table = self.soup.find('table', attrs={'class':'data'})
        currency_rows = currency_table.find_all('tr')
        rates = {}
        for row in currency_rows:
            columns = row.find_all('tr')
            if len(columns) >= 5:
                currency_name = columns[3].text.strip()
                currency_rate = float(columns[4].text.strip().replace(',', '.'))
                rates[currency_name] = currency_rate
        return rates

# URL страницы с курсами валют
url = 'https://www.cbr.ru/currency_base/daily/'

# создаем экземпляр класса CurrencyConverter с URL-адресом страницы
converter = CurrencyConverter(url)

# конвертируем 100 рублей в доллары США
rubles = 100
usd = converter.convert('RUB', 'USD', rubles)

print (f'{rubles} рублей равны {usd:.2f} долларам США.')
# вроде должно работать, но не очень понимаю из за чего ошибка