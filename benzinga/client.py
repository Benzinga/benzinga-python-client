import requests, json
import datetime as dt
import param_check
from benzinga_errors import (TokenAuthenticationError, RequestAPIEndpointError, IncorrectParameterEntry,
                             URLIncorrectlyFormattedError )

class Benzinga: 

    def __init__(self, api_token):

        self.token = api_token
        self.headers = {'accept': 'application/json'}
        self.url_dict = {"API v1": "https://api.benzinga.com/api/v1/" , "API v1.v1": "https://api.benzinga.com/api/v1.1/",
                         "API v2": "https://api.benzinga.com/api/v2/", "Data v3": "http://data-api.zingbot.bz/rest/v3/",
                         "Data v2": "https://data.benzinga.com/rest/v2/", "V3": "http://data-api.zingbot.bz/rest/v3/"}
        self.param_initiate = param_check.Param_Check()
        self.__token_check__(self.token)

    def __token_check__(self, api_token):
        end_date = dt.date.today().strftime('%Y-%m-%d')
        company_ticker = "AAPL"
        params = {'token': api_token, 'parameters[date_to]': end_date,
                  'parameters[tickers]': company_ticker}
        try:
            ratingsUrl = self.__url_call__("calendar", "dividends")
            ratings = requests.get(ratingsUrl, headers= self.headers, params=params)
            if ratings.status_code == 401:
                raise TokenAuthenticationError
        except TokenAuthenticationError as t:
            print("%sYour token is not valid. Please try again" % (t))


    def __url_call__(self, resource, sub_resource = ""):  # Private Method to modify requests calls
        endpoint_type = {"calendar": "%s%s/%s" % (self.url_dict["API v2"], resource, sub_resource),
                         "chart": "%s%s" % (self.url_dict["API v2"], resource),
                         "quote": "%s%s" % (self.url_dict["Data v2"], resource),
                         "batchhistory": "%s%s" % (self.url_dict["Data v2"], resource),
                         "autocomplete": "%s%s" % (self.url_dict["Data v2"], resource),
                         "instruments": "%s%s" % (self.url_dict["Data v3"], resource),
                         "quoteDelayed": "%s%s" % (self.url_dict["API v1"], resource),
                         "logos": "%s%s" % (self.url_dict["API v1.v1"], resource),
                         "fundamentals": "%s%s/%s" % (self.url_dict["V3"], resource, sub_resource),
                         "ownership": "%s%s/%s" % (self.url_dict["V3"], resource, sub_resource)}
        if resource not in endpoint_type:
            raise URLIncorrectlyFormattedError
        url_string = endpoint_type[resource]
        return url_string

    """Batch Request"""

    def batch_history(self, company_tickers = None):
        params = {"token": self.token, "symbol": company_tickers}
        self.param_initiate.fundamentals_check(params)
        try:
            batchhistory_url = self.__url_call__("batchhistory")
            batchhistory = requests.get(batchhistory_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return batchhistory.json()

    """Autocomplete"""

    def auto_complete(self, query = None, limit = None, search_method = None, exchanges = None, types = None):
        params = {"token": self.token, "query": query, "limit": limit, "searchMethod": search_method,
                  "exchanges": exchanges, "types": types}
        self.param_initiate.autocomplete_check(params)
        try:
            autocomplete_url = self.__url_call__("autocomplete")
            autocomplete = requests.get(autocomplete_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return autocomplete.json()

    """Security"""

    def security(self, company_tickers = None, cusip = None):
        params = {"token": self.token, "symbol": company_tickers, "cusip": cusip}
        self.param_initiate.security_check(params)
        try:
            security_url = self.__url_call__("quote")
            security = requests.get(security_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return security.json()

    """Quote"""

    def quote(self, company_tickers = None):
        params = {"token": self.token, "symbols": company_tickers}
        self.param_initiate.fundamentals_check(params)
        try:
            quote_url = self.__url_call__("quote")
            quote = requests.get(quote_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return quote.json()

    """Instruments"""

    def instruments(self, fields = None, query = None, date_from=None, date_to =None, date_asof=None,
                    sort_field=None, sort_dir=None):
        params = {"token": self.token, "fields": fields, "query":query, "start_date": start_date, "date_from":date_from,
                  "date_to":date_to, "date_asof": date_asof, "sortfield":sort_field, "sortdir":sort_dir}
        self.param_initiate.instruments_check(params)
        try:
            instruments_url = self.__url_call__("instruments")
            instruments = requests.get(instruments_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return instruments.json()

    "Calendar Oriented Data"

    def dividends(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None,
                  div_yield_operation=None, div_yield = None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to,
                  "parameters[tickers]":company_tickers,"parameters[importance]": importance,
                  "parameters[date_sort]": date_sort, "parameters[updated]": updated_params,
                  "paramaters[dividend_yield_operation]": div_yield_operation,
                  "parameters[dividend_yield]": div_yield}
        self.param_initiate.calendar_check(params)
        try:
            dividends_url = self.__url_call__("calendar", "dividends")
            dividends = requests.get(dividends_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return dividends.json()

    def earnings(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  :company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params}
        self.param_initiate.calendar_check(params)
        try:
            earnings_url = self.__url_call__("calendar", "earnings")
            earnings = requests.get(earnings_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return earnings.json()

    def splits(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  :company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params}
        self.param_initiate.calendar_check(params)
        try:
            splits_url = self.__url_call__("calendar", "splits")
            splits = requests.get(splits_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return splits.json()

    def economics(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                    company_tickers=None, importance=None, date_sort=None, updated_params=None, country=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  : company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params, "country": country}
        self.param_initiate.calendar_check(params)
        try:
            economics_url = self.__url_call__("calendar", "economics")
            economics = requests.get(economics_url, headers= self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return economics.json()

    def guidance(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                    company_tickers=None, importance=None, date_sort=None, updated_params=None, country=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  : company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params, "country": country}
        self.param_initiate.calendar_check(params)
        try:
            guidance_url = self.__url_call__("calendar", "guidance")
            guidance = requests.get(guidance_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return guidance.json()

    def ipo(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  :company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params}
        self.param_initiate.calendar_check(params)
        try:
            ipo_url = self.__url_call__("calendar", "ipos")
            ipo = requests.get(ipo_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return ipo.json()

    def retail(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  :company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params}
        self.param_initiate.calendar_check(params)
        try:
            retail_url = self.__url_call__("calendar", "retail")
            retail = requests.get(retail_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return retail.json()

    def ratings(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None, action=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  :company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params, "parameters[action]": action}
        self.param_initiate.calendar_check(params)
        try:
            ratings_url = self.__url_call__("calendar", "ratings")
            ratings = requests.get(ratings_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return ratings.json()

    def conference_calls(self, page=None, pagesize=None, base_date=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        params = {'token': self.token, "page": page, "pagesize": pagesize, "parameters[date]": base_date,
                  "parameters[date_from]": date_from, "parameters[date_to]": date_to, "parameters[tickers]"
                  :company_tickers, "parameters[importance]": importance, "parameters[date_sort]": date_sort,
                  "parameters[updated]": updated_params}
        self.param_initiate.calendar_check(params)
        try:
            conference_url = self.__url_call__("calendar", "conference-calls")
            conference = requests.get(conference_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return conference.json()

    """Financial Fundamentals"""

    def fundamentals(self, company_tickers=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_tickers, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            financials_url = self.__url_call__("fundamentals")
            financials = requests.get(financials_url, headers=self.headers, params= params)
            print(financials.url)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return financials.json()
    

    def financials(self, company_tickers=None, isin=None, cik=None, date_asof=None, period=None, reporttype=None):
        params = {'token': self.token, "symbols": company_tickers, "isin": isin, "cik": cik, "asOf": date_asof,
                  "period": period, "reportType": reporttype}
        self.param_initiate.fundamentals_check(params)
        try:
            financials_url = self.__url_call__("fundamentals", "financials")
            financials = requests.get(financials_url, headers=self.headers, params= params)
            print(financials.url)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return financials.json()

    def valuation_ratios(self, company_tickers=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_tickers, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            valuation_url = self.__url_call__("fundamentals", "valuationRatios")
            valuation = requests.get(valuation_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return valuation.json()

    def earning_ratios(self, company_tickers=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_tickers, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            earnings_url = self.__url_call__("fundamentals", "earningRatios")
            earnings = requests.get(earnings_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return earnings.json()

    def operation_ratios(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            operations_url = self.__url_call__("fundamentals", "operationRatios")
            operations = requests.get(operations_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return operations.json()

    def share_class(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            shareclass_url = self.__url_call__("fundamentals", "shareClass")
            shareclass = requests.get(shareclass_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return shareclass.json()

    def earning_reports(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            earningreports_url = self.__url_call__("fundamentals", "earningReports")
            earningreports = requests.get(earningreports_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return earningreports.json()

    def financial_statements(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            financialstatements_url = self.__url_call__("fundamentals", "financialStatements")
            financialstatements = requests.get(financialstatements_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return financialstatements.json()

    def alpha_beta(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            alphabeta_url = self.__url_call__("fundamentals", "alphaBeta")
            alphabeta = requests.get(alphabeta_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return alphabeta.json()

    def company_profile(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            companyprofile_url = self.__url_call__("fundamentals", "companyProfile")
            company_profile = requests.get(companyprofile_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return company_profile.json()

    def company(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            company_url = self.__url_call__("fundamentals", "company")
            company = requests.get(company_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return company.json()

    def share_class_profile_history(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            profilehistory_url = self.__url_call__("fundamentals", "shareClassProfileHistory")
            profilehistory = requests.get(profilehistory_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return profilehistory.json()

    def asset_classification(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            asset_url = self.__url_call__("fundamentals", "assetClassification")
            asset = requests.get(asset_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return asset.json()


    """Delayed Quotes"""

    def delayed_quote(self, company_tickers=None, isin=None, cik=None):
        params = {'token': self.token, "symbols": company_tickers, "isin": isin, "cik": cik}
        self.param_initiate.delayed_quote_check(params)
        try:
            delayedquote_url = self.__url_call__("quoteDelayed")
            delayedquote = requests.get(delayedquote_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return delayedquote.json()

    """Ownership"""

    def summary(self, company_ticker=None, isin=None, cik=None, date_asof=None):
        params = {'token': self.token, "symbols": company_ticker, "isin": isin, "cik": cik, "asOf": date_asof}
        self.param_initiate.fundamentals_check(params)
        try:
            summary_url = self.__url_call__("ownership", "summary")
            summary = requests.get(summary_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return summary.json()

    """Chart"""

    def chart(self, company_tickers, date_range, interval):
        params = {'symbol': company_tickers.upper(), 'from': date_range, 'interval': interval}
        url = self.__url_call__("Chart")
        chart = requests.get(url, headers=self.headers, params=params)
        return chart.json()

    def logos(self, company_tickers = None, filters = None):
        params = {"token": self.token, "symbols": company_tickers, "filters": filters}
        self.param_initiate.logos_check(params)
        try:
            logos_url = self.__url_call__("logos")
            logos = requests.get(logos_url, headers = self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return logos.json()


    """Output"""

    def JSON(self, func_output):
        result = json.dumps(func_output, indent= 4)
        print(result)
        return result

    def result(self, func_output):
        for object in func_output:
            print("You have the following options to display: ")
            for o in func_output[object][0]:
                print(o)

if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    false_token = 0
    company_tickers = "AAPL"
    start_date = "2018-01-01"
    sample_run = Benzinga(token)
    test = sample_run.batch_history(company_tickers="AAPL")
    sample_run.JSON(test)











    

