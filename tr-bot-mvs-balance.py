from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from time import sleep
from sys import exit
import time
import datetime
import smtplib

def find_quantity(total, price):
	quantity = float(total)/ float(price)
	return quantity

def balances_coins():
	global balanceBTC
	global balance
	global bitcoins
	global btc_coins
	global balancecoin1
	global balancecoin2
	global balancecoin3
	global balancecoin4
	global balancecoin5
	global coin1_coins
	global coin2_coins
	global coin3_coins
	global coin4_coins
	global coin5_coins
	
	#Balances
	balanceBTC = client.get_asset_balance(asset='BTC')
	balance = client.get_asset_balance('BTC')
	bitcoins = float(balance['free'])
	btc = format(bitcoins/1, '.8f')

	balancecoin1 = client.get_asset_balance(asset=coin1)
	balance = client.get_asset_balance(coin1)
	coin1_coins = float(balance['free'])
	coin1_coins = format(coin1_coins/1, '.8f')
	coin1_coins = find_quantity(coin1_coins, 1)

	balancecoin2 = client.get_asset_balance(asset=coin2)
	balance = client.get_asset_balance(coin2)
	coin2_coins = float(balance['free'])
	coin2_coins = format(coin2_coins/1, '.8f')
	coin2_coins = find_quantity(coin2_coins, 1)

	balancecoin3 = client.get_asset_balance(asset=coin3)
	balance = client.get_asset_balance(coin3)
	coin3_coins = float(balance['free'])
	coin3_coins = format(coin3_coins, '.8f')
	coin3_coins = find_quantity(coin3_coins, 1)

	balancecoin4 = client.get_asset_balance(asset=coin4)
	balance = client.get_asset_balance(coin4)
	coin4_coins = float(balance['free'])
	coin4_coins = format(coin4_coins, '.8f')
	coin4_coins = find_quantity(coin4_coins, 1)

	balancecoin5 = client.get_asset_balance(asset=coin5)
	balance = client.get_asset_balance(coin5)
	coin5_coins = float(balance['free'])
	coin5_coins = format(coin5_coins, '.8f')
	coin5_coins = find_quantity(coin5_coins, 1)

coin1 = 'ADA'
coin2 = 'XLM'
coin3 = 'ZEC'
coin4 = 'NEO'
coin5 = 'BTS'

#Binance API credentials
api_key = 'yourapikey'
api_pw = 'yourapipassword'

client = Client(api_key, api_pw)

balances_coins()

total_b_btc=0
btc_coin1 =0
btc_coin2 =0
btc_coin3 =0
btc_coin4 =0
btc_coin5 =0
btc_coins =0

#LastPrices
#****************** COIN1 ******************
sym1 = coin1 + "BTC"
klines = client.get_historical_klines(sym1, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

while not klines:
	klines = client.get_historical_klines(sym1, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")	

most_recent = klines.pop()
last_closing_coin1 = most_recent[4]
last_closing_coin1 = float(last_closing_coin1)
last_closing_coin1 = format(last_closing_coin1/1, '.8f')
last_closing_coin1 = find_quantity(last_closing_coin1, 1)

#****************** COIN2 ******************
sym2 = coin2 + "BTC"
klines = client.get_historical_klines(sym2, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

while not klines:
	klines = client.get_historical_klines(sym2, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

most_recent = klines.pop()
last_closing_coin2 = most_recent[4]                               

last_closing_coin2 = float(last_closing_coin2)
last_closing_coin2 = format(last_closing_coin2/1, '.8f')
last_closing_coin2 = find_quantity(last_closing_coin2, 1)

#****************** COIN3 ******************
sym3 = coin3 + "BTC"
klines = client.get_historical_klines(sym3, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

while not klines:
	klines = client.get_historical_klines(sym3, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

most_recent = klines.pop()
last_closing_coin3 = most_recent[4]                               

last_closing_coin3 = float(last_closing_coin3)
last_closing_coin3 = format(last_closing_coin3/1, '.8f')
last_closing_coin3 = find_quantity(last_closing_coin3, 1)

#****************** COIN4 ******************
sym4 = coin4 + "BTC"
klines = client.get_historical_klines(sym4, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

while not klines:
	klines = client.get_historical_klines(sym4, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

most_recent = klines.pop()
last_closing_coin4 = most_recent[4]                               

last_closing_coin4 = float(last_closing_coin4)
last_closing_coin4 = format(last_closing_coin4/1, '.8f')
last_closing_coin4 = find_quantity(last_closing_coin4, 1)

#****************** COIN5 ******************
sym5 = coin5 + "BTC"
klines = client.get_historical_klines(sym5, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

while not klines:
	klines = client.get_historical_klines(sym5, Client.KLINE_INTERVAL_1MINUTE, "1 min ago UTC")

most_recent = klines.pop()
last_closing_coin5 = most_recent[4]                               

last_closing_coin5 = float(last_closing_coin5)
last_closing_coin5 = format(last_closing_coin5/1, '.8f')
last_closing_coin5 = find_quantity(last_closing_coin5, 1)

#BTC Value Calculation

btc_coin1 = coin1_coins * last_closing_coin1
btc_coin1 = '{0:.8f}'.format(btc_coin1)
btc_coin1 = float(btc_coin1)

btc_coin2 = coin2_coins * last_closing_coin2
btc_coin2 = '{0:.8f}'.format(btc_coin2)
btc_coin2 = float(btc_coin2)

btc_coin3 = coin3_coins * last_closing_coin3
btc_coin3 = '{0:.8f}'.format(btc_coin3)
btc_coin3 = float(btc_coin3)

btc_coin4 = coin4_coins * last_closing_coin4
btc_coin4 = '{0:.8f}'.format(btc_coin4)
btc_coin4 = float(btc_coin4)

btc_coin5 = coin5_coins * last_closing_coin5
btc_coin5 = '{0:.8f}'.format(btc_coin5)
btc_coin5 = float(btc_coin5)

total_b_btc = btc_coin1+btc_coin2+btc_coin3+btc_coin4+btc_coin5+bitcoins

total_b_btc = '{0:.8f}'.format(total_b_btc)
total_b_btc = float(total_b_btc)

msg1 = "Original Balance - Balance BTC %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s" % (bitcoins,coin1,coin1_coins,coin2,coin2_coins,coin3,coin3_coins,coin4,coin4_coins,coin5,coin5_coins)

msg2 = "Balance in BTC - Balance BTC %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s" % (bitcoins,coin1,btc_coin1,coin2,btc_coin2,coin3,btc_coin3,coin4,btc_coin4,coin5,btc_coin5)

bal = "Total BTC: %s" % (total_b_btc)
print(bal)
print("\n")
print(msg1)
print("\n")
print(msg2)

sym = input('> ')
