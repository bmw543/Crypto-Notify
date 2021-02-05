import requests
from bs4 import BeautifulSoup
import numpy as np
from win10toast import ToastNotifier
import os

# coins

coins = np.array([["Stellar", "https://www.coindesk.com/price/stellar", 0.30, 0.30],
                  ["Algorand", "https://www.coindesk.com/price/algorand", 0.70, 0.76],
                  ["Bitcoin Cash", "https://www.coindesk.com/price/bitcoin-cash", 400, 480],
                  ["Bitcoin", "https://www.coindesk.com/price/bitcoin", 34000, 39000],
                  ["Litecoin", "https://www.coindesk.com/price/litecoin", 140, 160]])

filepath = os.path.dirname(os.path.realpath(__file__))
icons_path = filepath + "/crypto_icons/"

class Coin():

    def __init__(self, name, url, low_price, high_price):
        self.name = name
        self.url = url
        self.low_price = float(low_price)
        self.high_price = float(high_price)

    def get_price(self):
        html = requests.get(self.url)
        soup = BeautifulSoup(html.content, "html.parser")
        results = soup.find(id="export-chart-element")
        self.price = float(results.find(class_="price-large").text[1:].replace(",", ""))

for coin in coins:
    coin = Coin(coin[0], coin[1], coin[2], coin[3])
    coin.get_price()
    notification = ToastNotifier()
    if (coin.price < coin.low_price):
        notification.show_toast(coin.name, coin.name + " has fallen below $" + str(coin.low_price), duration=20, icon_path=icons_path + coin.name + ".ico", threaded = True)
    if (coin.price > coin.high_price):
        notification.show_toast(coin.name, coin.name + " has risen above $" + str(coin.high_price), duration=20, icon_path=icons_path + coin.name + ".ico", threaded = True)

