#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests, json, sys, os, warnings
import pandas as pd
import datetime as dt
import numpy as np

class Benzinga:
    
    def __init__(self, api_token):
        token = api_token 
        
    def __url_call__(self, part_one, part_two): #Private Method to modify requests calls 
        url_string = "https://api.benzinga.com/api/v2/" + part_one + "/" + part_two + "/"
        headers = {'accept': 'application/json'}
        params = {'token': token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,                  'parameters[tickers]': company_ticker}
        return url_string
        
    def ratings(self, company_ticker, start_date, end_date = "", interval = "1D"):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d') #if the user doesn't enter a end date, the current date is the default date
        ratingsUrl = self.__url_call__("calendar", "ratings")
        ratings = requests.get(ratingsUrl, headers=headers, params=params)
        return ratings.json()
    
    def financials(self, company_ticker, start_date, end_date = "", interval = "1D"):
        
        

if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    sample_run = Benzinga(token)
    print(sample_run.ratings("AAPL", "2019-01-01"))
    
    

