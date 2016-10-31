from http import client
from datetime import datetime
from relativedelta import relativedelta
from itertools import chain
import time
import math

import ijson

class Tradier():
	def __init__(self):
		tradier_key = open('../tradier.key', 'r').read()
		self.connection = client.HTTPSConnection('sandbox.tradier.com', 443, timeout=30)
		self.headers = {
			"Accept":"application/json",
			"Authorization":"Bearer {}".format(tradier_key)
		}

	def get_history(self, symbol, months):
		current_data = datetime.now()
		start = datetime.now() - relativedelta(months=months)

		start = start.strftime("%Y-%m-%d")
		end = current_data.strftime("%Y-%m-%d")

		request = '/v1/markets/history?symbol={0}&interval=daily&start={1}&end={2}'.format(symbol, start, end)
		self.connection.request('GET', request, None, self.headers)
		try:
			response = self.connection.getresponse()
			return response

		except client.HTTPException:
			return 'Exception'

	def get_one_year_history(self, symbol):
		return self.get_history(symbol, 12)

	def get_moving_average_history(self, symbol, days):
		history = []
		averages = []
		raw_history = ijson.items(self.get_one_year_history(symbol), 'history.day.item')

		for day in raw_history:
			history.append({'date': day['date'], 'close': day['close']})

		for i in range(days, len(history) + 1):
			last_elements = list(chain(history[i-days:i]))
			moving_average = sum([e['close'] for e in last_elements]) / days
			averages.append({'date': history[i-1]['date'], 'movingAverage': moving_average})

		return averages

	def get_moving_average(self, symbol, days):
		history = []
		averages = []
		months_necessary = math.ceil(days / 22)
		raw_history = ijson.items(self.get_history(symbol, months_necessary), 'history.day.item')

		for day in raw_history:
			history.append({'date': day['date'], 'close': day['close']})

		last_elements = list(chain(history[-days:]))
		moving_average = sum([e['close'] for e in last_elements]) / days

		return moving_average