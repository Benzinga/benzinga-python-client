#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests, json, sys, os, warnings
import pandas as pd
import datetime as dt
import numpy as np

class BenzingaError():
    pass

class Benzinga:
    def __init__(self, api_token):
        self.token = api_token 
        self.headers = {'accept': 'application/json'}
        
    def __url_call__(self, part_one, part_two): #Private Method to modify requests calls 
        url_string = "https://api.benzinga.com/api/v2/" + part_one + "/" + part_two + "/"
        return url_string

    def alternative__url_call__(self, part_one): #Private Method to modify requests calls 
        url_string = "https://data.benzinga.com/rest/v2/" + part_one
        return url_string

    def ratings(self, company_ticker, start_date, end_date = "", interval = "1D"):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d') #if the user doesn't enter a end date, the current date is the default date
        url = self.__url_call__("calendar", "ratings")
        params = {'token': token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date, 'parameters[tickers]': company_ticker}
        ratings = requests.get(url, headers=self.headers, params=params) 
        return ratings.json()
    
    def financials(self, company_ticker, start_date, end_date = "", interval = "1D"):
        print("need to be here so doesn't give me indentation error")


    def chart(self, ticker, date_range, interval):
        url = self.alternative__url_call__("chart")
        params = {'symbol': ticker.upper(), 'from': date_range, 'interval': interval}
        chart = requests.get(url, headers=self.headers, params=params)
        return chart.json()

if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    sample_run = Benzinga(token)
    print(json.dumps(sample_run.chart('AAPL', '1Y', '1W'), indent=4))
    

