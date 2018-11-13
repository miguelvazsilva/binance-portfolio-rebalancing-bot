# binance-portfolio-rebalancing-bot
This Python script, allows you to mantain a portfolio of binance coins, using the Threshold Rebalancing Strategy

<h2>Requirements</h2>
This bot requires the Binance Exchange API Python implementation for automated trading. Download it and install, via pip:
https://github.com/sammchardy/python-binance

<h2>Strategy</h2>
This bot buys altcoins (maximum 5), each one with a configured percentage of the global portfolio(valued in BTC), with all the BTC in the account, and will rebalance the portfolio, triggered by the coins that have the percentage of the global portfolio, with higher deviation, than the one configured in the bot.

<h2>Example</h2>
Initial configuration of the bot:
<ul><li>rebalance %  = 5</li>
<li>coin1 = 'ADA' - coin1perc = 30</li>
<li>coin2 = 'XLM' - coin2perc = 20</li>
<li>coin3 = 'ZEC' - coin3perc = 30</li>
<li>coin4 = 'NEO' - coin4perc = 10</li>
<li>coin5 = 'BTS' - coin5perc = 10</li></ul>

The coins are bought with all the BTC in the account, and the initial deviation would be something like this (the bot automatically prints this information in the screen):
<ul><li>15:00:36.684000
<li>Deviation Rebalance ADA 0.01%</li>
<li>Deviation Rebalance XLM -0.02%</li>
<li>Deviation Rebalance ZEC -0.01%</li>
<li>Deviation Rebalance NEO 0.02%</li>
<li>Deviation Rebalance BTS 0%</li></ul>

After a while, the distribution deviation would be something like this (the bot automatically prints this information in the screen):

<ul><li>18:00:36.684000
<li>Deviation Rebalance ADA 6.2%</li>
<li>Deviation Rebalance XLM -3.2%</li>
<li>Deviation Rebalance ZEC -1%</li>
<li>Deviation Rebalance NEO 1%</li>
<li>Deviation Rebalance BTS -3%</li></ul>

The bot would automatically sell ADA because it passed the rebalance percentage of 5%, and with the BTC, it would try to buy XLM, ZEC and BTS (only if the buy order was of more than 0.001 BTC that is the binance trading minimum LOT).

Whenever a buy or sell order is made, a email is sent by SMTP, with some trade information.

<h2>Configuration</h2>

Configure the email notifications:
<ul><li>server = smtplib.SMTP('smtp.gmail.com', 587)</li>
<li>server.login("youremail@gmail.com", "your password")</li></ul>

Configure the Binance API credentials:
<ul><li>api_key = 'yourapikey'</li>
<li>api_pw = 'yourapipassword'</li></ul>

Configure the rebalance deviation percentage:
rebal  = 5

Configure the altcoins and respective portfolio percentages:
<ul><li>coin1 = 'ADA'</li>
<li>coin2 = 'XLM'</li>
<li>coin3 = 'ZEC'</li>
<li>coin4 = 'NEO'</li>
<li>coin5 = 'BTS'</li>
<li>coin1perc = 30</li>
<li>coin2perc = 20</li>
<li>coin3perc = 30</li>
<li>coin4perc = 10</li>
<li>coin5perc = 10</li></ul>

<h2>Execution</h2>

Run the script "tr-bot-mvs.py".

If you want to check the balances at any moment, you can use the script "tr-bot-mvs-balance.py" (configure the coin tickers and api information).

<h2>Disclaimer and Important Information:</h2>
<ul><li>This bot does not guarantee profits.</li>
<li>This bot works with Buy/Sell Market Orders.</li></ul>
