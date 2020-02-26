import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time 

#--------------------------------------------------------------------------
# Script that sends realtime stock data for MSFT to excel every 60 seconds.
#--------------------------------------------------------------------------

# Modify line 9 to include an actual API key. Your own personalized key can be found on the alphaVantage website.
api_key = 'XXXXXXXXXXXXXXXX'

ts = TimeSeries(key=api_key, output_format='pandas')
i=1
while i==1:
	data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
	data_ts.to_excel("output.xlsx") 		#This sends updated real time stock data to output.xlsx
	time.sleep(60) 			