import pandas as pd
from yahoofinancials import YahooFinancials
import datetime

all_tickers = ["AAPL", "MSFT", "AMZN"]

# extracting stock data (historical close price) for the stocks identified
close_prices = pd.DataFrame()
end_date = (datetime.date.today()).strftime('%Y-%m-%d')
beg_date = (datetime.date.today()-datetime.timedelta(3000)).strftime('%Y-%m-%d')
cp_tickers = all_tickers
attempt = 0
drop = []
while len(cp_tickers) != 0 and attempt <=5:
    print("-----------------")
    print("attempt number ",attempt)
    print("-----------------")
    cp_tickers = [j for j in cp_tickers if j not in drop]
    for i in range(len(cp_tickers)):
        try:
            print("currently in: " + cp_tickers[i])
            yahoo_financials = YahooFinancials(cp_tickers[i])
            print(yahoo_financials)
            json_obj = yahoo_financials.get_historical_price_data(beg_date, end_date, "daily")
            print(json_obj)
            ohlv = json_obj[cp_tickers[i]]['prices']
            temp = pd.DataFrame(ohlv)[["formatted_date","adjclose"]]
            print(temp)
            temp.set_index("formatted_date",inplace=True)
            temp2 = temp[~temp.index.duplicated(keep='first')] #Keeps only the first instance of duplicated values.
            close_prices[cp_tickers[i]] = temp2["adjclose"]
            drop.append(cp_tickers[i]) 
            print(temp2)
            print("closes prices ")
            print(close_prices)
        except:
            print(cp_tickers[i]," :failed to fetch data...retrying")
            continue
    attempt+=1