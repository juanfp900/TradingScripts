import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------
# This script plots closing price and SMA line over 1min intervals in a graph using matplotlib
#----------------------------------------------------------------------------------------------


# Modify line 13 to include an actual API key. Your own personalized key can be found on the alphaVantage website
api_key = 'XXXXXXXXXXXXXXXX'

ts = TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')

# SMA values on the graph are calculated by taking the average of the stock price over the past 60 minutes
period = 60
ti = TechIndicators(key=api_key, output_format='pandas')
data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min', time_period=period, series_type='close')


df1 = data_ti 
df2 = data_ts['4. close'].iloc[period-1::]

df2.index = df1.index 						


total_df = pd.concat([df1, df2], axis=1)


# Plots the real time data into a chart with an x and y axis
plt.figure(figsize=(16,8))
plt.title('Close Price History', fontsize=18)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)


plt.plot(total_df)

plt.show()