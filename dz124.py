import requests

class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        try:
            # API НБУ для курсу валют
            url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json'
            response = requests.get(url)
            data = response.json()
            return data[0]['rate']
        except Exception as e:
            print("Помилка при отриманні курсу долара:", e)
            return None

    def convert_to_usd(self, amount_uah):
        if self.usd_rate is None:
            print("Неможливо конвертувати валюту через відсутність курсу.")
            return None
        return round(amount_uah / self.usd_rate, 2)


if __name__ == "__main__":
    converter = CurrencyConverter()
    try:
        uah_amount = float(input("Введіть суму в гривнях: "))
        usd_amount = converter.convert_to_usd(uah_amount)
        if usd_amount is not None:
            print(f"{uah_amount} грн = {usd_amount} USD за курсом НБУ {converter.usd_rate} грн/долар")
    except ValueError:
        print("Будь ласка, введіть числове значення.")
