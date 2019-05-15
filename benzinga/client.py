import requests, json
import datetime as dt
import benzinga_errors

class Benzinga:

    def __init__(self, api_token):

        self.token = api_token
        self.headers = {'accept': 'application/json'}
        self.url_dict = {"API v1": "https://api.benzinga.com/api/v1" ,"API v2": "https://api.benzinga.com/api/v2/",
                         "Data v3": "http://data-api.zingbot.bz/rest/v3/","Data v2": "https://data.benzinga.com/rest/v2/"}
        self.endpoint_type = {"Calendar / Fundamentals": self.url_dict["API v2"], "Charts": self.url_dict["Data v2"],
                              "Instruments": self.url_dict["Data v3"]}

    def __url_call__(self, type , part_one = "", part_two = ""):  # Private Method to modify requests calls
        if type == "Calendar / Fundamentals":
            url_string = self.endpoint_type[type] + str("%s/%s"%(part_one, part_two))
        elif type == "Charts":
            url_string = self.endpoint_type[type] + "chart"
        elif type == "Instruments":
            url_string = self.endpoint_type[type] + "instruments"

        return url_string

    def instruments(self, company_ticker = "", start_date = "", end_date = ""): #testing right now
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {}
        instrumentsUrl = self.__url_call__("Instruments")
        instruments = requests.get(instrumentsUrl, headers=self.headers, params=params)
        return instruments.json()


    "Calendar Oriented Data"

    def dividends(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}

            dividendsUrl = self.__url_call__("Calendaer / Fundamentals", "calendar", "dividends")

            dividends = requests.get(dividendsUrl, headers=self.headers, params=params)

        raise benzinga_errors.API_Endpoint_Error("")
        return dividends.json()

    def earnings(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        earningsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "earnings")
        earnings = requests.get(earningsUrl, headers = self.headers, params= params)
        return earnings.json()

    def splits(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        splitsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "splits")
        splits = requests.get(splitsUrl, headers = self.headers, params= params)
        return splits.json()

    def econonomics(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        economicsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "economics")
        economics = requests.get(economicsUrl, headers = self.headers, params= params)
        return economics.json()

    def guidance(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        guidanceUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "dividends")
        guidance = requests.get(guidanceUrl, headers = self.headers, params= params)
        return guidance.json()

    def ipo(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        ipoUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "ipos")
        ipo = requests.get(ipoUrl, headers = self.headers, params= params)
        return ipo.json()

    def retail(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        retailUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "retail")
        retail = requests.get(retailUrl, headers = self.headers, params= params)
        return retail.json()

    def ratings(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        ratingsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "dividends")
        ratings = requests.get(ratingsUrl, headers= self.headers, params=params)
        return ratings.json()

    def conference_call(self, company_ticker, start_date, end_date = ""):
        if not end_date:
            end_date = dt.date.today().strftime('%Y-%m-%d')
        params = {'token': self.token, 'parameters[date_from]': start_date, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        conferenceUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "conference_call")
        conference = requests.get(conferenceUrl, headers = self.headers, params= params)
        return conference.json()

    """Financial Fundamentals"""
    

    def financials(self, company_ticker, asof, period = "12M", reportType = "TTM"):
        params = {'token': self.token, "symbols" : company_ticker,
                  "asOf": asof, "period": period, "report type": reportType}
        financialsUrl = self.__url_call__("Calendar / Fundamentals", "fundamentals", "financials")
        financials = requests.get(financialsUrl, headers = self.headers, params= params)
        return financials.json()

    def valuation_ratios(self, company_ticker, asof):
        params = {'token': self.token, "symbols": company_ticker, "asOf": asof}
        valuationsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "valuationRatios")
        valuation = requests.get(valuationsUrl, headers = self.headers, params = params)
        return valuation.json()

    def earning_ratios(self, company_ticker, asof):
        params = {'token': self.token, "symbols": company_ticker, "asOf": asof}
        earningsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "earningRatios")
        earnings = requests.get(earningsUrl, headers = self.headers, params= params)
        return earnings.json()

    def operations_ratios(self, company_ticker, asof):
        params = {'token': self.token, "symbols": company_ticker, "asOf": asof}
        operationsUrl = self.__url_call__("Calendar / Fundamentals", "calendar", "operationRatios")
        operations = requests.get(operationsUrl, headers=self.headers, params= params)
        return operations.json()


    def chart(self, ticker, date_range, interval):
        params = {'symbol': ticker.upper(), 'from': date_range, 'interval': interval}
        url = self.__url_call__("Chart")
        chart = requests.get(url, headers=self.headers, params=params)
        return chart.json()

    """Delayed Quotes"""

    def delayed_quote(self, company_ticker):
        params = {'token': self.token, "symbols": company_ticker}
        delayedquoteUrl = self.__url_call__("quoteDelayed", "earningRatios")
        delayedquote = requests.get(delayedquoteUrl, headers=self.headers, params=params)
        return delayedquote.json()

if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    company_ticker = "AAPL"
    start_date = "2018-01-01"
    sample_run = Benzinga(token)
    sample_run.dividends(company_ticker, start_date)





    

