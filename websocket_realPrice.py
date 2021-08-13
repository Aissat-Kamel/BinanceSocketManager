from binance_client import client
from binance.websockets import BinanceSocketManager
import time
#import telegram_interface


kline = {}


def spd(msg):
	"""
	{
		"E": 1499404907056,				# event time
		"s": "ETHBTC",					# symbol
		"k": {
			"t": 1499404860000, 		# start time of this bar
			"T": 1499404919999, 		# end time of this bar
			"s": "ETHBTC",				# symbol
			"i": "1m",					# interval
			"f": 77462,					# first trade id
			"L": 77465,					# last trade id
			"o": "0.10278577",			# open
			"c": "0.10278645",			# close
			"h": "0.10278712",			# high
			"l": "0.10278518",			# low
			"v": "17.47929838",			# volume
			"n": 4,						# number of trades
			"x": false,					# whether this bar is final
			"q": "1.79662878",			# quote volume
			"V": "2.34879839",			# volume of active buy
			"Q": "0.24142166",			# quote volume of active buy
			"B": "13279784.01349473"	# can be ignored
			}
	}
	"""

	kline[msg["s"]] = msg["k"]["c"]


bm = BinanceSocketManager(client)
tickers = ["BTCUSDT", "ADAUSDT", "LTCUSDT"]
for ticker in tickers:
	conn_key = bm.start_kline_socket(ticker, spd, "1h")

bm.start()

time.sleep(6)

alert = 0
prev_volume = 0
volume_now = float(kline["BTCUSDT"])
prev_volume = volume_now

while True:
	volume_now = float(kline["BTCUSDT"])
	diff = volume_now - prev_volume
	if diff >= 0:
		print(diff)
	time.sleep(5)
	prev_volume = volume_now
