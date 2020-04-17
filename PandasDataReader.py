#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:49:58 2020

@author: Juanp
"""


import pandas as pd
import pandas_datareader.data as pdr
import datetime


class PandasDataReader:
    global stock_cp


    def getFinanicalInfo(stock_cp):
        tickers = ["AMZN", "FB", "APP"]
        print("hi")
        stock_cp = pd.DataFrame() # dataframe to store close price of each ticker
        attempt = 0 
        drop = [] # initializing list to store tickers whose close price was successfully extracted
        while len(tickers) != 0 and attempt <= 5:
            tickers = [j for j in tickers if j not in drop] # removing stocks whose data has been extracted from the ticker list
            for i in range(len(tickers)):
                try:
                    temp = pdr.get_data_yahoo(tickers[i],datetime.date.today()-datetime.timedelta(1095),datetime.date.today())
                    temp.dropna(inplace = True)
                    stock_cp[tickers[i]] = temp["Adj Close"]
                    drop.append(tickers[i])       
                except:
                    print(tickers[i]," :failed to fetch data...retrying")
                    continue
            attempt+=1
            return stock_cp
    
 
    
def main():
    p = PandasDataReader();
    stock_cp = p.getFinanicalInfo()
    print(stock_cp)

if __name__== "__main__":
    main()
    