import requests
from bs4 import BeautifulSoup
import time
from .models import Exchange, Price


def parse_to_float(text):
    """
    convert string to float
    :param text:
    :return: Float text
    """
    return float(text)


def payplux():
    exchange = Exchange.objects.get(name="Payplux")
    url = "https://payplux.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price_table = soup.findChildren('table')
    rows = price_table[0].find_all('tr')
    btc_price = payplux_btc(rows[2])
    eth_price = payplux_eth(rows[3])
    ltc_price = payplux_ltc(rows[4])
    bch_price = payplux_bch(rows[5])
    prices = [btc_price, ltc_price, eth_price, bch_price]
    new_price = Price(
        exchange=exchange.id,
        btc_price=btc_price,
        ltc_price=ltc_price,
        eth_price=eth_price,
        bch_price=bch_price
    )
    new_price.save()
    return prices


def payplux_btc(btc_row):
    btc_columns = btc_row.find_all('td')
    btc_price = btc_columns[1].find('strong').text[1:]
    btc_price = parse_to_float(btc_price)
    return btc_price


def payplux_ltc(ltc_row):
    ltc_columns = ltc_row.find_all('td')
    ltc_price = ltc_columns[1].find('strong').text[1:]
    ltc_price = parse_to_float(ltc_price)
    return ltc_price


def payplux_eth(eth_row):
    eth_columns = eth_row.find_all('td')
    eth_price = eth_columns[1].find('strong').text[1:]
    eth_price = parse_to_float(eth_price)
    return eth_price


def payplux_bch(bch_row):
    bch_columns = bch_row.find_all('td')
    bch_price = bch_columns[1].find('strong').text[1:]
    bch_price = parse_to_float(bch_price)
    return bch_price

payplux()
