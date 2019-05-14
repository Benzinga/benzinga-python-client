import requests, json
import datetime as dt

class Benzinga:
    
    def __init__(self, api_token):
        self.token = api_token
        self.headers = {'accept': 'application/json'}
        
    def __url_call__(self, part_one, part_two):
        url_string = str("https://api.benzinga.com/api/v2/%s/%s/"% (part_one, part_two))
        return url_string

    "Calendar Oriented Data"

    def dividends(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        dividendsUrl = self.__url_call__("calendar", "dividends")
        dividends = requests.get(dividendsUrl, headers = self.headers, params= params)
        return dividends.json()

    def earnings(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        earningsUrl = self.__url_call__("calendar", "earnings")
        earnings = requests.get(earningsUrl, headers = self.headers, params= params)
        return earnings.json()

    def splits(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        splitsUrl = self.__url_call__("calendar", "splits")
        splits = requests.get(splitsUrl, headers = self.headers, params= params)
        return splits.json()

    def econonomics(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        economicsUrl = self.__url_call__("calendar", "economics")
        economics = requests.get(economicsUrl, headers = self.headers, params= params)
        return economics.json()

    def guidance(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        guidanceUrl = self.__url_call__("calendar", "guidance")
        guidance = requests.get(guidanceUrl, headers = self.headers, params= params)
        return guidance.json()

    def ipo(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        ipoUrl = self.__url_call__("calendar", "ipos")
        ipo = requests.get(ipoUrl, headers = self.headers, params= params)
        return ipo.json()

    def retail(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        retailUrl = self.__url_call__("calendar", "retail")
        retail = requests.get(retailUrl, headers = self.headers, params= params)
        return retail.json()

    def ratings(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        ratingsUrl = self.__url_call__("calendar", "ratings")
        ratings = requests.get(ratingsUrl, headers= self.headers, params=params)
        return ratings.json()

    def conference_call(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        conferenceUrl = self.__url_call__("calendar", "conference-calls")
        conference = requests.get(conferenceUrl, headers = self.headers, params= params)
        return conference.json()

    """Financial Fundamentals"""
    
    def financials(self, company_ticker, asof, period = "12M", reportType = "TTM"):
        params = {'token': self.token, "symbols" : company_ticker,
                  "asOf": asof, "period": period, "report type": reportType}
        financialsUrl = self.__url_call__("fundamentals", "financials")
        financials = requests.get(financialsUrl, headers = self.headers, params= params)
        return financials.json()

    def valuation_ratios(self, company_ticker, asof):
        params = {'token': self.token, "symbols": company_ticker, "asOf": asof}
        valuationsUrl = self.__url_call__("fundamentals", "valuationRatios")
        valuation = requests.get(valuationsUrl, headers = self.headers, params = params)
        return valuation.json()

    def earning_ratios(self, company_ticker, asof):
        params = {'token': self.token, "symbols": company_ticker, "asOf": asof}
        earningsUrl = self.__url_call__("fundamentals", "earningRatios")
        earnings = requests.get(earningsUrl, headers = self.headers, params= params)
        return earnings.json()

    def operations_ratios(self, company_ticker, asof):
        params = {'token': self.token, "symbols": company_ticker, "asOf": asof}
        operationsUrl = self.__url_call__("fundamentals", "earningRatios")
        operations = requests.get(operationsUrl, headers=self.headers, params= params)
        return operations.json()

if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    sample_run = Benzinga(token)
    sample_run.ratings("AAPL", start_date = "2019-01-01") #tested
    print(json.dumps(sample_run.financials("TSLA", asof = "2018-01-01"), indent= 4))
    sample_run.valuation_ratios("AAPL", "2018-01-01")
    sample_run.earning_ratios("AAPL", "2018-01-01")
    sample_run.operations_ratios("AAPL", "2018-01-01")


    
    

