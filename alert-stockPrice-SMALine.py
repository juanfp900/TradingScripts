import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from twilio.rest import Client
import time 
import sys

#-----------------------------------------------------------------------------------------
# Script that sends text notification every time a stock price is below or above SMA line
# Alert to buy if stock price is below SMA line in real time. 
# Alert to sell if price is above SMA Line in real time.
#-----------------------------------------------------------------------------------------

# Modify line 15 to include an actual API key. Your own personalized key can be found on the alphaVantage website.
api_key = 'XXXXXXXXXXXXXXXX' 

# Modify line 18 to include Twilio Account SID and Auth Token. Your own personalized SID and token can be found after creating Twilio account
client = Client("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                       
            
ts = TimeSeries(key=api_key, output_format='pandas') 
ti = TechIndicators(key=api_key, output_format='pandas')

i = 1
period = 60
while i==1:
	data_ts, meta_data_ts = ts.get_intraday(symbol="MSFT", outputsize='compact')
	data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min', time_period=period, series_type='close')
	df2 = data_ts['4. close']

	currentStockPrice = df2[0]
	print(currentStockPrice)

	df1 = data_ti['SMA']
	currentAveragePrice = df1[1]
	print(currentAveragePrice)
	if currentStockPrice > currentAveragePrice:
		print("Time to sell")
		client.messages.create(to="############",		# Phone number to send message to hide this
                       from_="#############",  			# Twilio number that sends notification
                       body="Time to sell MSFT stock")
	else:
		print("Time to buy")
		client.messages.create(to="############",		# Phone number you want to send notification to
                       from_="############",  			# Twilio number that sends notification
                       body="Time to buy MSFT stock!")
	time.sleep(15) 										#loop every 15 seconds. 60/15=4 since we can only call API 5 times every 60 seconds.


	
