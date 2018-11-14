from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from time import sleep
from sys import exit
import time
import datetime
import smtplib

#Email Notifications
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("youremail@gmail.com", "your password")

#From a total quantity, calculate the number of coins
def find_quantity(total, price):
    quantity = float(total)/ float(price)
    return quantity

#Calculate the current balance of the coins
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
    
    #Balance BTC
    balanceBTC = client.get_asset_balance(asset='BTC')
    balance = client.get_asset_balance('BTC')
    bitcoins = float(balance['free'])
    btc_coins = bitcoins

    #Balance Coin1
    balancecoin1 = client.get_asset_balance(asset=coin1)
    balance = client.get_asset_balance(coin1)
    coin1_coins = float(balance['free'])
    coin1_coins = format(coin1_coins/1, '.8f')
    coin1_coins = find_quantity(coin1_coins, 1)

    #Balance Coin2
    balancecoin2 = client.get_asset_balance(asset=coin2)
    balance = client.get_asset_balance(coin2)
    coin2_coins = float(balance['free'])
    coin2_coins = format(coin2_coins/1, '.8f')
    coin2_coins = find_quantity(coin2_coins, 1)

    #Balance Coin3
    balancecoin3 = client.get_asset_balance(asset=coin3)
    balance = client.get_asset_balance(coin3)
    coin3_coins = float(balance['free'])
    coin3_coins = format(coin3_coins, '.8f')
    coin3_coins = find_quantity(coin3_coins, 1)

    #Balance Coin4
    balancecoin4 = client.get_asset_balance(asset=coin4)
    balance = client.get_asset_balance(coin4)
    coin4_coins = float(balance['free'])
    coin4_coins = format(coin4_coins, '.8f')
    coin4_coins = find_quantity(coin4_coins, 1)

    #Balance Coin5
    balancecoin5 = client.get_asset_balance(asset=coin5)
    balance = client.get_asset_balance(coin5)
    coin5_coins = float(balance['free'])
    coin5_coins = format(coin5_coins, '.8f')
    coin5_coins = find_quantity(coin5_coins, 1)

def btc_value():
    global btc_coin1
    global btc_coin2
    global btc_coin3
    global btc_coin4
    global btc_coin5
    global total_b_btc
    
    #BTC Value Calculation
    btc_coin1 = coin1_coins * last_closing_coin1
    btc_coin1 = float(btc_coin1)

    btc_coin2 = coin2_coins * last_closing_coin2
    btc_coin2 = float(btc_coin2)

    btc_coin3 = coin3_coins * last_closing_coin3
    btc_coin3 = float(btc_coin3)

    btc_coin4 = coin4_coins * last_closing_coin4
    btc_coin4 = float(btc_coin4)

    btc_coin5 = coin5_coins * last_closing_coin5
    btc_coin5 = float(btc_coin5)

    total_b_btc = btc_coin1+btc_coin2+btc_coin3+btc_coin4+btc_coin5+bitcoins

def deviation():
    global deviation_coin1
    global deviation_coin2
    global deviation_coin3
    global deviation_coin4
    global deviation_coin5
    global dif_dev_coin1
    global dif_dev_coin2
    global dif_dev_coin3
    global dif_dev_coin4
    global dif_dev_coin5
    
    deviation_coin1 = (btc_coin1/total_b_btc)*100
    deviation_coin1 = format(round(deviation_coin1,2))
    deviation_coin1 = float(deviation_coin1)
    dif_dev_coin1 = deviation_coin1-coin1perc
    dif_dev_coin1 = format(round(dif_dev_coin1 ,2))
    dif_dev_coin1  = float(dif_dev_coin1)

    deviation_coin2 = (btc_coin2/total_b_btc)*100
    deviation_coin2 = format(round(deviation_coin2,2))
    deviation_coin2 = float(deviation_coin2)
    dif_dev_coin2 = deviation_coin2-coin2perc
    dif_dev_coin2 = format(round(dif_dev_coin2 ,2))
    dif_dev_coin2  = float(dif_dev_coin2)

    deviation_coin3 = (btc_coin3/total_b_btc)*100      
    deviation_coin3 = format(round(deviation_coin3,2))
    deviation_coin3 = float(deviation_coin3)
    dif_dev_coin3 = deviation_coin3-coin3perc
    dif_dev_coin3 = format(round(dif_dev_coin3 ,2))
    dif_dev_coin3  = float(dif_dev_coin3)

    deviation_coin4 = (btc_coin4/total_b_btc)*100      
    deviation_coin4 = format(round(deviation_coin4,2))
    deviation_coin4 = float(deviation_coin4)
    dif_dev_coin4 = deviation_coin4-coin4perc
    dif_dev_coin4 = format(round(dif_dev_coin4 ,2))
    dif_dev_coin4  = float(dif_dev_coin4)

    deviation_coin5 = (btc_coin5/total_b_btc)*100      
    deviation_coin5 = format(round(deviation_coin5,2))
    deviation_coin5 = float(deviation_coin5)
    dif_dev_coin5 = deviation_coin5-coin5perc
    dif_dev_coin5 = format(round(dif_dev_coin5 ,2))
    dif_dev_coin5  = float(dif_dev_coin5)

#Buy order 
def buy_order(buycoin,coin,rebalcoin,sym):          

    global total_b_btc

    buycoin = -1*float(buycoin)
    rebalcoin = -1*float(rebalcoin)
    rebalcoin = '{0:.8f}'.format(rebalcoin)
    

    print("Buying %s of %s, with BTC %s:") % (buycoin,coin,rebalcoin)
    print("Method 1: Buy method round quantity 8 decimal places:")
    try:
        client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin, 8), newClientOrderId=1)
    except BinanceAPIException as e:
        print("Method 1 failed.")
        print("Method 2: Buy method round quantity 3 decimal places")
        if "LOT_SIZE" in e.message:
            try:
                client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin, 3), newClientOrderId=1)
            except BinanceAPIException as e:
                print("Method 2 failed.")
                print(e.message)
                print("Method 3: Buy method round quantity 2 decimal places")
                try:
                    client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin, 2), newClientOrderId=1)
                except BinanceAPIException as e:
                    print(e.message)
                    print("Method 3 failed.")
                    print("Method 4: Buy method rounded")
                    try:
                        client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin), newClientOrderId=1)
                    except BinanceAPIException as e:
                        print("Method 4 failed.")
                        print(e.message)
                        print("Buy method rounded")
                        try:
                            buycoin=buycoin-1
                            client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin), newClientOrderId=1)
                        except BinanceAPIException as e:
                            print("Method 5 failed.")
                            print(e.message)
                            print("Buy method -1")
                            try:
                                buycoin=buycoin-4
                                client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin), newClientOrderId=1)
                            except BinanceAPIException as e:
                                print("Method 6 failed.")
                                print(e.message)
                                print("Buy method -5")
                                try:
                                    buycoin=buycoin+6
                                    buycoin=buycoin-0.1
                                    client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin, 2), newClientOrderId=1)
                                except BinanceAPIException as e:
                                    print("Method 7 failed.")
                                    print(e.message)
                                    print("Buy method -0.1")
                                    try:
                                        buycoin=buycoin-0.1
                                        client.create_order(symbol=sym, side="BUY", type="MARKET", quantity=round(buycoin, 2), newClientOrderId=1)
                                    except BinanceAPIException as e:
                                        print("Method 8 failed.")
                                        print(e.message)
                                        print("Buy method -0.2")
                                        return
    
    pcoin = total_b_btc/5
    pcoin = '{0:.8f}'.format(pcoin)
    total_b_btc = '{0:.8f}'.format(total_b_btc)

    balances_coins()
    btc_value()

    subject = "Purchase Notification %s, Quantity %s | BTC Value %s" % (coin,buycoin,rebalcoin)
    msg1 = "Purchase %s Notification | Quantity: %s | BTC Value %s \n\n" % (coin,buycoin,rebalcoin)
    msg2 = "Balance BTC %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s\n\n" % (bitcoins,coin1,coin1_coins,coin2,coin2_coins,coin3,coin3_coins,coin4,coin4_coins,coin5,coin5_coins)
    msg3 = "Balance in BTC - Balance BTC %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s" % (bitcoins,coin1,btc_coin1,coin2,btc_coin2,coin3,btc_coin3,coin4,btc_coin4,coin5,btc_coin5)
    msg = msg1 + msg2 + msg3
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail("youremail@gmail.com", "yourdestinationemail@gmail.com", message)
    print("\n")
    print(msg)
    print("\n")
    total_b_btc= float(total_b_btc)
               
#Sell order
def sell_order(sellcoin,coin,rebalcoin,sym):
    global total_b_btc
    
    print("Selling %s of %s, with BTC %s:") % (sellcoin,coin,rebalcoin)
    print("Method 1: Sell method round quantity 8 decimal places:")
    try:
        client.create_order(symbol=sym, side="SELL", type="MARKET", quantity=round(sellcoin, 8), newClientOrderId=1)
    except BinanceAPIException as e:
        print("Method 1 failed.")
        print("Method 2: Sell method round quantity 3 decimal places")
        if "LOT_SIZE" in e.message:
            try:
                client.create_order(symbol=sym, side="SELL", type="MARKET", quantity=round(sellcoin, 3), newClientOrderId=1)
            except BinanceAPIException as e:
                print("Method 2 failed.")
                print(e.message)
                print("Method 3: Sell method round quantity 2 decimal places")
                try:
                    client.create_order(symbol=sym, side="SELL", type="MARKET", quantity=round(sellcoin, 2), newClientOrderId=1)
                except BinanceAPIException as e:
                    print(e.message)
                    print("Method 3 failed.")
                    print("Method 4: Sell method rounded")
                    try:
                        client.create_order(symbol=sym, side="SELL", type="MARKET", quantity=round(sellcoin), newClientOrderId=1)
                    except BinanceAPIException as e:
                        print("Method 4 failed.")
                        print(e.message)
                        print("Sell method rounded")
                        return

    pcoin = total_b_btc/5
    pcoin = '{0:.8f}'.format(pcoin)
    total_b_btc = '{0:.8f}'.format(total_b_btc)

    balances_coins()
    btc_value()

    subject = "Sales Notification %s %s | BTC %s" % (coin,sellcoin,rebalcoin)
    msg1 = "Rebalance %s Notification | %s %s%s | %s %s%s | %s %s%s | %s %s%s | %s %s%s\n\nTotal BTC %s\n" % (coin, coin1,dif_dev_coin1,"%",coin2,dif_dev_coin2,"%",coin3,dif_dev_coin3,"%",coin4,dif_dev_coin4,"%",coin5,dif_dev_coin5,"%",total_b_btc)
    msg2 = "Per coin %s\n\n" % (pcoin)
    msg3 = msg1+msg2+"%s-BTC %s | Rebalance BTC %s | Trade %s\n%s-BTC %s | Rebalance BTC %s | Trade %s\n%s-BTC %s | Rebalance BTC %s | Trade %s\n%s-BTC %s | Rebalance BTC %s | Trade %s\n%s-BTC %s | Rebalance BTC %s | Trade %s\n\n" % (coin1,btc_coin1,rebalcoin1,sellcoin1,coin2,btc_coin2,rebalcoin2,sellcoin2,coin3,btc_coin3,rebalcoin3,sellcoin3,coin4,btc_coin4,rebalcoin4,sellcoin4,coin5,btc_coin5,rebalcoin5,sellcoin5)
    msg4 = "Balance BTC %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s | Balance %s %s" % (bitcoins,coin1,coin1_coins,coin2,coin2_coins,coin3,coin3_coins,coin4,coin4_coins,coin5,coin5_coins)
    msg = msg3 + "Sales Notification %s %s | BTC %s \n" % (coin,sellcoin,rebalcoin) + msg4
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail("youremail@gmail.com", "yourdestinationemail@gmail.com", message)
    print("\n")
    print(msg)
    print("\n")
    total_b_btc= float(total_b_btc)

#Main

#Binance API credentials
api_key = 'yourapikey'
api_pw = 'yourapipassword'

client = Client(api_key, api_pw)

#Rebalance % | Coins | Coin Distribution %:
rebal  = 5
coin1 = 'ADA'
coin2 = 'XLM'
coin3 = 'ZEC'
coin4 = 'NEO'
coin5 = 'BTS'
coin1perc = 30
coin2perc = 20
coin3perc = 30
coin4perc = 10
coin5perc = 10

if (coin1perc+coin2perc+coin3perc+coin4perc+coin5perc) != 100:
    print("The total percentage of the coins must be 100%")
    exit()

if (rebal) <= 0:
    print("Rebalance % must be configured with a valid number")
    exit()

balances_coins()

count = 0

while count < 52595:
    
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

    #LastPrices
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

    #LastPrices
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

    #LastPrices
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

    #LastPrices
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

    btc_value()
    
    deviation()
    
    print(datetime.datetime.now().time())

    print("Deviation Rebalance " + coin1 + " " + str(dif_dev_coin1) + "%")
    print("Deviation Rebalance " + coin2 + " " + str(dif_dev_coin2) + "%")
    print("Deviation Rebalance " + coin3 + " " + str(dif_dev_coin3) + "%")
    print("Deviation Rebalance " + coin4 + " " + str(dif_dev_coin4) + "%")
    print("Deviation Rebalance " + coin5 + " " + str(dif_dev_coin5) + "%\n") 

    #Sell Condition
    if (dif_dev_coin1 > rebal or dif_dev_coin2 > rebal or dif_dev_coin3 > rebal or dif_dev_coin4 > rebal or dif_dev_coin5 > rebal):
        rebalcoin1 = total_b_btc*(float(coin1perc)/100)
        rebalcoin1 = btc_coin1 - rebalcoin1
        sellcoin1 = rebalcoin1/last_closing_coin1

        rebalcoin2 = total_b_btc*(float(coin2perc)/100)
        rebalcoin2 = btc_coin2 - rebalcoin2
        sellcoin2 = rebalcoin2/last_closing_coin2

        rebalcoin3 = total_b_btc*(float(coin3perc)/100)
        rebalcoin3 = btc_coin3 - rebalcoin3
        sellcoin3 = rebalcoin3/last_closing_coin3

        rebalcoin4 = total_b_btc*(float(coin4perc)/100)
        rebalcoin4 = btc_coin4 - rebalcoin4
        sellcoin4 = rebalcoin4/last_closing_coin4

        rebalcoin5 = total_b_btc*(float(coin5perc)/100)
        rebalcoin5 = btc_coin5 - rebalcoin5
        sellcoin5 = rebalcoin5/last_closing_coin5

        rebalcoin1 = '{0:.3f}'.format(rebalcoin1)
        rebalcoin2 = '{0:.3f}'.format(rebalcoin2)
        rebalcoin3 = '{0:.3f}'.format(rebalcoin3)
        rebalcoin4 = '{0:.3f}'.format(rebalcoin4)
        rebalcoin5 = '{0:.3f}'.format(rebalcoin5)

        btc_coin1 = '{0:.8f}'.format(btc_coin1)
        btc_coin2 = '{0:.8f}'.format(btc_coin2)
        btc_coin3 = '{0:.8f}'.format(btc_coin3)
        btc_coin4 = '{0:.8f}'.format(btc_coin4)
        btc_coin5 = '{0:.8f}'.format(btc_coin5)
                        
        if (dif_dev_coin1 > rebal):
            sell_order(sellcoin1,coin1,rebalcoin1,sym1)
                        
        if (dif_dev_coin2 > rebal):
            sell_order(sellcoin2,coin2,rebalcoin2,sym2)

        if (dif_dev_coin3 > rebal):
            sell_order(sellcoin3,coin3,rebalcoin3,sym3)

        if (dif_dev_coin4 > rebal):
            sell_order(sellcoin4,coin4,rebalcoin4,sym4)
                
        if (dif_dev_coin5 > rebal):
            sell_order(sellcoin5,coin5,rebalcoin5,sym5)
                
        balances_coins()
    
    #Buy Condition    
    if (bitcoins > 0.001):
    
        btc_value()
    
        deviation()
        
        rebalcoin1 = total_b_btc*(float(coin1perc)/100)
        rebalcoin1 = btc_coin1 - rebalcoin1
        buycoin1 = rebalcoin1/last_closing_coin1

        rebalcoin2 = total_b_btc*(float(coin2perc)/100)
        rebalcoin2 = btc_coin2 - rebalcoin2
        buycoin2 = rebalcoin2/last_closing_coin2

        rebalcoin3 = total_b_btc*(float(coin3perc)/100)
        rebalcoin3 = btc_coin3 - rebalcoin3
        buycoin3 = rebalcoin3/last_closing_coin3

        rebalcoin4 = total_b_btc*(float(coin4perc)/100)
        rebalcoin4 = btc_coin4 - rebalcoin4
        buycoin4 = rebalcoin4/last_closing_coin4

        rebalcoin5 = total_b_btc*(float(coin5perc)/100)
        rebalcoin5 = btc_coin5 - rebalcoin5
        buycoin5 = rebalcoin5/last_closing_coin5

        btc_coin1 = '{0:.8f}'.format(btc_coin1)
        btc_coin2 = '{0:.8f}'.format(btc_coin2)
        btc_coin3 = '{0:.8f}'.format(btc_coin3)
        btc_coin4 = '{0:.8f}'.format(btc_coin4)
        btc_coin5 = '{0:.8f}'.format(btc_coin5)
        
        if (buycoin1 < 0 and rebalcoin1 < -0.001):
            buy_order(buycoin1,coin1,rebalcoin1,sym1)
                        
        if (buycoin2 < 0 and rebalcoin2 < -0.001):
            buy_order(buycoin2,coin2,rebalcoin2,sym2)

        if (buycoin3 < 0 and rebalcoin3 < -0.001):
            buy_order(buycoin3,coin3,rebalcoin3,sym3)

        if (buycoin4 < 0 and rebalcoin4 < -0.001):
            buy_order(buycoin4,coin4,rebalcoin4,sym4)
                
        if (buycoin5 < 0 and rebalcoin5 < -0.001):
            buy_order(buycoin5,coin5,rebalcoin5,sym5)
                
        balances_coins()
                                         
    count = count + 1
    time.sleep(10)
