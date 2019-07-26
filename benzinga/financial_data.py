import requests, json
import datetime as dt
from .param_check import Param_Check
from .benzinga_errors import (TokenAuthenticationError, RequestAPIEndpointError, IncorrectParameterEntry,
                             URLIncorrectlyFormattedError, MissingParameter, AccessDeniedError)


class Benzinga: 

    def __init__(self, api_token):
        self.token = api_token
        self.headers = {'accept': 'application/json'}
        self.url_dict = {
            "API v1": "https://api.benzinga.com/api/v1/", 
            "API v1.v1": "https://api.benzinga.com/api/v1.1/",
            "API v2": "https://api.benzinga.com/api/v2/",
            "Data v2": "https://data.benzinga.com/rest/v2/", 
            "V3": "https://api.benzinga.io/dataapi/rest/v3/",
            "Data api v2": "https://api.benzinga.io/dataapi/rest/v2/",
            "API rest": "https://data.benzinga.com/quote-store/api/",
            "IO API": "https://api.benzinga.io/data/rest/"
        }
        self.param_initiate = Param_Check()

    def __token_check(self, api_token):
        """Private Method: Token check is a private method that does a basic check for whether the api token has
        access to the fundamentals and/or calendar data. Different tokens have access to different endpoints.
        Disregard the error if your request is fullfilled but the token authentication error is raised.

         Arguments:
             API Token.

         Returns:
             Token authentication error if token is invalid."""

        end_date = dt.date.today().strftime('%Y-%m-%d')
        company_ticker = "AAPL"
        params = {
            'token': api_token,
            'parameters[date_to]': end_date,
            'parameters[tickers]': company_ticker
        }

        ratingsUrl = self.__url_call("calendar", "dividends")
        ratings = requests.get(ratingsUrl, headers=self.headers, params=params)
        if ratings.status_code == 401:
            raise TokenAuthenticationError

    def __url_call(self, resource, sub_resource=""):
        """Private Method: URL Call is used to take input from the public methods and return the appropriate url format
        for the endpoint. For example, the resource is calendar and the subresource might be ratings. The correct
        url endpoint call is created by using these two.

        Arguments:
            Resource and Sub- Resource

        Returns:
            url for the endpoint call"""

        endpoint_type = {
            "calendar": "%s%s/%s" % (self.url_dict["API v2"], resource, sub_resource),
            "quote": "%s%s" % (self.url_dict["Data v2"], resource),
            "security": "%s%s" % (self.url_dict["Data api v2"], resource),
            "chart": "%s%s" % (self.url_dict["Data api v2"], resource),
            "batchhistory": "%s%s" % (self.url_dict["Data api v2"], resource),
            "autocomplete": "%s%s" % (self.url_dict["Data v2"], resource),
            "instruments": "%s%s" % (self.url_dict["V3"], resource),
            "quoteDelayed": "%s%s" % (self.url_dict["API v1"], resource),
            "logos": "%s%s" % (self.url_dict["API v1.v1"], resource),
            "fundamentals": "%s%s/%s" % (self.url_dict["V3"], resource, sub_resource),
            "ownership": "%s%s/%s" % (self.url_dict["V3"], resource, sub_resource),
            "movers": "%s%s/%s" % (self.url_dict["IO API"], resource, sub_resource),
            "tickerDetail": "%s%s" % (self.url_dict["V3"], resource)
        }
        if resource not in endpoint_type:
            raise URLIncorrectlyFormattedError
        url_string = endpoint_type[resource]
        return url_string

    def price_history(self, company_tickers, date_from, date_to):
        """Public Method: Benzinga Price History requires 3 required arguments. It returns daily candles for a specific date range
         for a company. The from and to date is required along with the company ticker. 
         
         Arguments:
             Required - company_tickers (str)
             Required - date_from (str) - "YYYY-MM-DD"
             Required - date_to (str) - "YYYY-MM-DD"
         
         Returns:
             Daily candles for the company for a specific date range"""
        
        revised_input = "%s:%s:%s" % (company_tickers, date_from, date_to)
        params = {
            "symbol": revised_input,
            "apikey": self.token
        }
        self.param_initiate.batchhistory_check(params)
        try:
            batchhistory_url = self.__url_call("batchhistory")
            batchhistory = requests.get(batchhistory_url, headers=self.headers, params=params)
            if batchhistory.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return batchhistory.json()

    def auto_complete(self, company_tickers, limit=None, search_method=None, exchanges=None, types=None):
        """Public Method: Benzinga Auto-Complete returns the relevant information related to a company
        ticker.

        Arguments:
            Required - company_tickers (str)
            Optional:
            limit (int) - Limits the number of results to input.
            search_method (str) - You can enter either "SYMBOL", which does a prefix match on symbol, or
            "SYMBOL_NAME" which does a prefix match on symbol and prefix match on any word in the name, or
            you can enter "SYMBOL_WITHIN" which matches any part of the symbol.
            exchanges (str) If this value is present, then it will only include those exchanges.
            types (str) You can enter either "STOCK", "TYPE" or "OEF".

        Returns:
            Relevant information such as company name of short name, type and exchange"""

        params = {
            "token": self.token,
            "query": company_tickers,
            "limit": limit,
            "searchMethod": search_method,
            "exchanges": exchanges,
            "types": types
        }
        self.param_initiate.autocomplete_check(params)
        try:
            autocomplete_url = self.__url_call("autocomplete")
            autocomplete = requests.get(autocomplete_url, headers=self.headers, params=params)
            if autocomplete.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return autocomplete.json()

    def security(self, company_tickers, cusip=None):
        """Public Method: Benzinga Security returns the information regarding the security.

        Arguments:
            Required - company_tickers (str)
            Optional:
            cusip (str)

        Returns:
            Symbol, exchange symbol, exchange, country, currency, cusip and description """

        params = {
            "apikey": self.token,
            "symbol": company_tickers,
            "cusip": cusip
        }
        self.param_initiate.security_check(params)
        try:
            security_url = self.__url_call("security")
            security = requests.get(security_url, headers=self.headers, params=params)
            if security.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return security.json()

    def chart(self, company_tickers, date_from, date_to=None, interval=None, session=None):
        """Public Method: Benzinga Chart looks at detailed price values over a period of time.

                Arguments:
                    Required - company_tickers (str)
                    Required - date_from (str) - For date_from, you can enter "YTD" for the first trading day
                    of the year. "1d", "5d" or "1m". You can also enter the date from in the "YY-MM-DD"format too.
                    Optional:
                    date_to (str) - "YY-MM-DD"
                    interval (str) - "1MONTH", "1W", "1D", "1H", "15M". Default: "5M"
                    session (str) - "ANY", "REGULAR"

                Returns:
                    open, high, low, close, volume, time, dateTime"""
        params = {
            "apikey": self.token,
            "symbol": company_tickers,
            "from": date_from,
            "to": date_to,
            "interval": interval,
            "session": session
        }
        self.param_initiate.charts_check(params)
        try:
            chart_url = self.__url_call("chart")
            chart = requests.get(chart_url, headers=self.headers, params=params)
            if chart.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return chart.json()


    def quote(self, company_tickers):
        """Public Method: Benzinga Quote looks at many different attributes of the ticker like high, low, close etc

        Arguments:
            Required - company_tickers (str)

        Returns:
            symbol, dxsymbol, exchange, bzexchange, isoexchange, type, name, description, open
        high, low, close, bid price, ask price, ask size, size, bid time, ask time, last trade price, last
        trade time, volume, change, change percent, previous close price, fifty day average price,
        fifty two week high, fifty two week low, dividend yield, price/earnings, forward price/earnings,
        payout ratio, shares outstanding, open interest, shares per contract, multiplier"""

        params = {
            "token": self.token,
            "symbols": company_tickers
        }
        self.param_initiate.fundamentals_check(params)
        try:
            quote_url = self.__url_call("quote")
            quote = requests.get(quote_url, headers=self.headers, params=params)
            if quote.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return quote.json()

    def instruments(self, date_from=None, date_to =None, date_asof=None, market_cap_gt = None,
                    market_cap_lt= None, close_gt = None, sector = None, sort_field=None, sort_dir=None):
        """Public Method: Benzinga Instruments looks at all of the screener data with price statistics, based
         on different attributes.

         Arguments:
             Optional:
             date_from (str) - "YYYY-MM-DD"
             date_to (str) - "YYYY-MM-DD"
             date_asof (str) - "YYYY-MM-DD"
             market_cap_gt (str) - market cap greater than "1b" etc
             market_cap_lt (str) - market cap less than "1b" etc
             close_gt (str) - close price greater than.
             sector (str) - sector like "healthcare"
             sort field (str) - field to sort by (un-tested)
             sortdir (str) - direction of sort (un-tested)

         Returns:
             all of the data related to the instrument including marketcap, sector, company name
         etc, that can be found on the Benzinga Pro screener."""

        fields = "symbol,marketcap,exchange," \
                 "isin,country,name,previousClose,open,close,change,changePercent,sector"
        if market_cap_gt is not None:
            market_cap_greater = ";marketcap_gt_%s" % market_cap_gt
        else:
            market_cap_greater = ""
        if market_cap_lt is not None:
            marketcap_less = ";marketcap_lt_%s" % market_cap_lt
        else:
            marketcap_less = ""
        if close_gt is not None:
            close_greater = ";close_gt_%s" % close_gt
        else:
            close_greater = ""
        if sector is not None:
            sector = ";sector_in_%s" % sector
        else:
            sector = ""
        if market_cap_gt is None and market_cap_lt is None and close_gt is None and sector is None:
            query = None
        else:
            query = "%s%s%s%s" % (market_cap_greater, marketcap_less, close_greater, sector)
        params = {
            "apikey": self.token,
            "fields": fields,
            "query": query,
            "from": date_from,
            "to": date_to,
            "asOf": date_asof,
            "sortfield": sort_field,
            "sortdir": sort_dir
        }
        self.param_initiate.instruments_check(params)
        try:
            instruments_url = self.__url_call("instruments")
            instruments = requests.get(instruments_url, headers=self.headers, params=params)
            if instruments.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return instruments.json()

    def dividends(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None,
                  div_yield_operation=None, div_yield = None):
        """Public Method: Benzinga Dividends looks at the relevant dividend information for a
         company.

         Arguments:
             Optional:
             page (int) - page offset
             pagesize (int) - limit of results returned
             date_asof (str) - "YYYY-MM-DD"
             date_from (str) - "YYYY-MM-DD"
             date_to (str) - "YYYY-MM-DD"
             company_tickers (str)
             importance - (int) - not tested yet.
             date_sort - (str) - Dividend date field to sort on
             updated_params (int64) - records last updated unix time stamp. Forces the
             sort order to be greater or equal to the time stamp indicated.
             div_yield_operation (str) - to filter the div yield by for eg. "gt", "gte",
             "eq", "lte", "lt". Not tested
             div_yield (int) - div yield amount fo filter by. "1" for 100% or above.

         Returns:
             the id, date, updated, isin, ticker, name, exchange, frequency, dividend,
             dividend prior, dividend type, dividend yield, ex-dividend date, payable date,
             record date, importance
             """
        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params,
            "paramaters[dividend_yield_operation]": div_yield_operation,
            "parameters[dividend_yield]": div_yield
        }
        self.param_initiate.calendar_check(params)
        try:
            dividends_url = self.__url_call("calendar", "dividends")
            dividends = requests.get(dividends_url, headers=self.headers, params=params)
            if dividends.status_code == 401:
                raise AccessDeniedError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return dividends.json()

    def earnings(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        """Public Method: Benzinga Earnings looks at the quarterly earnings reports for different
        companies.

        Arguments:
            Optional:
             page (int) - page offset
             pagesize (int) - limit of results returned
             date_asof (str) - "YYYY-MM-DD"
             date_from (str) - "YYYY-MM-DD"
             date_to (str) - "YYYY-MM-DD"
             company_tickers (str)
             importance - (int) - not tested yet.
             date_sort - (str) - Dividend date field to sort on
             updated_params (int64) - records last updated unix time stamp. Forces the
             sort order to be greater or equal to the time stamp indicated.

        Returns:
            id, date, date confirmed, time, isin, ticker, exchange, name, period, period_year,
            eps, eps_est, eps_prior, eps_surprise, eps_surprise_percent, revenue, revenue est,
            revenue_prior, revenue_surprise, revenue_surprise_percent, importance, updated


        """
        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params
        }
        self.param_initiate.calendar_check(params)
        try:
            earnings_url = self.__url_call("calendar", "earnings")
            earnings = requests.get(earnings_url, headers=self.headers, params=params)
            if earnings.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return earnings.json()

    def splits(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        """Public Method: Benzinga Splits looks at the stock splits calendar data

                Arguments:
                    Optional:
                     page (int) - page offset
                     pagesize (int) - limit of results returned
                     date_asof (str) - "YYYY-MM-DD"
                     date_from (str) - "YYYY-MM-DD"
                     date_to (str) - "YYYY-MM-DD"
                     company_tickers (str)
                     importance - (int) - not tested yet.
                     date_sort - (str) - Dividend date field to sort on
                     updated_params (int64) - records last updated unix time stamp. Forces the
                     sort order to be greater or equal to the time stamp indicated.

                Returns:
                    id, updated, date, time, ticker, exchange, importance, ratio, optionable,
                    date_ex, date_recorded, date_distribution"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params
        }
        self.param_initiate.calendar_check(params)
        try:
            splits_url = self.__url_call("calendar", "splits")
            splits = requests.get(splits_url, headers=self.headers, params=params)
            if splits.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return splits.json()

    def economics(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                     importance=None, date_sort=None, updated_params=None, country=None):
        """Public Method: Benzinga Economics looks at different economic events in a country.

                Arguments:
                    Optional:
                     page (int) - page offset
                     pagesize (int) - limit of results returned
                     date_asof (str) - "YYYY-MM-DD"
                     date_from (str) - "YYYY-MM-DD"
                     date_to (str) - "YYYY-MM-DD"
                     company_tickers (str)
                     importance - (int) - not tested yet.
                     date_sort - (str) - Dividend date field to sort on
                     updated_params (int64) - records last updated unix time stamp. Forces the
                     sort order to be greater or equal to the time stamp indicated.
                     country (str) - 3 digit country code

                Returns:
                    id, date, time, country, event_name, event_period, period_year, actual, actual_t
                    consensus, consensus_t, prior, importance, updated, description"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params,
            "country": country
        }
        self.param_initiate.calendar_check(params)
        try:
            economics_url = self.__url_call("calendar", "economics")
            economics = requests.get(economics_url, headers=self.headers, params=params)
            if economics.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return economics.json()

    def guidance(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                    company_tickers=None, importance=None, date_sort=None, updated_params=None, country=None):
        """Public Method: Benzinga Guidance looks at different attributes like revenue guidance etc.
            Arguments:
                Optional:
                 page (int) - page offset
                 pagesize (int) - limit of results returned
                 date_asof (str) - "YYYY-MM-DD"
                 date_from (str) - "YYYY-MM-DD"
                 date_to (str) - "YYYY-MM-DD"
                 company_tickers (str)
                 importance - (int) - not tested yet.
                 date_sort - (str) - Dividend date field to sort on
                 updated_params (int64) - records last updated unix time stamp. Forces the
                 sort order to be greater or equal to the time stamp indicated.
                 country (str) - 3 digit country code

            Returns:
                id, date, time, ticker, exchange, name, period, period_year, prelim, eps_guidance_est,
                eps_guidance_max, eps_guidance_min, eps_guidance_prior_max, eps_guidance_prior_min,
                revenue_guidance_est, revenue_guidance_max, revenue_guidance_min, revenue_guidance_prior_max
                , revenue_guidance_prior_min, importance, updated"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params,
            "country": country
        }
        self.param_initiate.calendar_check(params)
        try:
            guidance_url = self.__url_call("calendar", "guidance")
            guidance = requests.get(guidance_url, headers=self.headers, params=params)
            if guidance.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return guidance.json()

    def ipo(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        """Public Method: Benzing IPO looks at initial public offering data for companies.

            Arguments:
                Optional:
                page (int) - page offset
                pagesize (int) - limit of results returned
                date_asof (str) - "YYYY-MM-DD"
                date_from (str) - "YYYY-MM-DD"
                date_to (str) - "YYYY-MM-DD"
                company_tickers (str)
                importance - (int) - not tested yet.
                date_sort - "str" - Dividend date field to sort on
                updated_params (int64) - records last updated unix time stamp. Forces the
                sort order to be greater or equal to the time stamp indicated.

            Returns:
                id, date, time, ticker, exchange, name, pricing_date, price_min, price_max, deal_status,
                insider_lockup_days, insider_lockup_date, offering_value, offering_shares, lead_underwriters,
                underwriter_quiet_expiration_days, underwriter_quiet_expiration_date, update"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params
        }
        self.param_initiate.calendar_check(params)
        try:
            ipo_url = self.__url_call("calendar", "ipos")
            ipo = requests.get(ipo_url, headers=self.headers, params=params)
            if ipo.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return ipo.json()

    def retail(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None):
        """Public Method: Benzinga Retail looks at retail data.

            Arguments:
                Optional:
                page (int) - page offset
                pagesize (int) - limit of results returned
                date_asof (str) - "YYYY-MM-DD"
                date_from (str) - "YYYY-MM-DD"
                date_to (str) - "YYYY-MM-DD"
                company_tickers (str)
                importance - (int) - not tested yet.
                date_sort - (str) - Dividend date field to sort on
                updated_params (int64) - records last updated unix time stamp. Forces the
                sort order to be greater or equal to the time stamp indicated.

            Returns:
                id, date, time, ticker, exchange, name, importance, period, period_year, sss,
                sss_est, retail_surprise, updated"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params
        }

        self.param_initiate.calendar_check(params)
        try:
            retail_url = self.__url_call("calendar", "retail")
            retail = requests.get(retail_url, headers=self.headers, params=params)
            if retail.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return retail.json()

    def ratings(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                  company_tickers=None, importance=None, date_sort=None, updated_params=None, action=None):
        """Public Method: Benzinga Ratings looks at ratings from different firms.

                Arguments:
                    Optional:
                    page (int) - page offset
                    pagesize (int) - limit of results returned
                    date_asof (str) - "YYYY-MM-DD"
                    date_from (str) - "YYYY-MM-DD"
                    date_to (str) - "YYYY-MM-DD"
                    company_tickers (str)
                    importance - (int) - not tested yet.
                    date_sort - (str) - Dividend date field to sort on
                    updated_params (int64) - records last updated unix time stamp. Forces the
                    sort order to be greater or equal to the time stamp indicated.
                    action - (str) - " Upgrades , Downgrades , Maintains , Lowers , Raises ,
                    Initiates Coverage On , Terminates Coverage On"

                Returns:
                    id, date, time, ticker, exchange, name, action_pt, action_company, rating_current,
                    pt_current, rating_prior, pt_prior, url, importance, updated, url_calendar, url_news,
                    analyst, analyst_name"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params,
            "parameters[action]": action
        }

        self.param_initiate.calendar_check(params)
        try:
            ratings_url = self.__url_call("calendar", "ratings")
            ratings = requests.get(ratings_url, headers=self.headers, params=params)
            if ratings.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return ratings.json()

    def conference_calls(self, page=None, pagesize=None, date_asof=None, date_from=None, date_to=None,
                            company_tickers=None, importance=None, date_sort=None, updated_params=None):
        """Public Method: Benzinga Conference calls looks at conference calls.

            Arguments:
                Optional:
                page (int) - page offset
                pagesize (int) - limit of results returned
                date_asof (str) - "YYYY-MM-DD"
                date_from (str) - "YYYY-MM-DD"
                date_to (str) - "YYYY-MM-DD"
                company_tickers (str)
                importance - (int) - not tested yet.
                date_sort - "str" - Dividend date field to sort on
                updated_params (int64) - records last updated unix time stamp. Forces the
                sort order to be greater or equal to the time stamp indicated.

            Returns:
                id, date, time, ticker, exchange, name, start_time, phone_num, international_line,
                reservation_num, access_code, webcase_url, importance, updated"""

        params = {
            'token': self.token,
            "page": page,
            "pagesize": pagesize,
            "parameters[date]": date_asof,
            "parameters[date_from]": date_from,
            "parameters[date_to]": date_to,
            "parameters[tickers]": company_tickers,
            "parameters[importance]": importance,
            "parameters[date_sort]": date_sort,
            "parameters[updated]": updated_params
        }
        self.param_initiate.calendar_check(params)
        try:
            conference_url = self.__url_call("calendar", "conference-calls")
            conference = requests.get(conference_url, headers=self.headers, params=params)
            if conference.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return conference.json()

    def fundamentals(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Fundamentals looks at overall financial data for a company.

        Arguments:
            Required - company_tickers (str)
            Optional:
                isin (str) - specifies company data to return.
                cik (str) - cik identifier
                date_asof (str) "YYYY-MM-DD"

        Returns:
            company, companyProfile, shareClass, earningReports, financialStatements, operation earning and valuation
            ratios, alphaBeta
        """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            financials_url = self.__url_call("fundamentals")
            financials = requests.get(financials_url, headers=self.headers, params= params)
            if financials.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return financials.json()
    

    def financials(self, company_tickers, isin=None, cik=None, date_asof=None, period=None, reporttype=None):
        """Public Method: Benzinga Financials looks at overall financial data like  for a company.

            Arguments:
                Required - company_tickers (str)
                Optional:
                    isin (str) - specifies company data to return.
                    cik (str) - cik identifier
                    date_asof (str) - "YYYY-MM-DD"
                    period (str) - select from (3M , 6M , 9M , 12M , 1Y)
                    reporttype (str) - select from (TTM, A (default), R,P)

            Returns:
                company, financials such as balance sheet information, assets and liabilities
                """
        params = {
            'token': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof,
            "period": period,
            "reportType": reporttype
        }

        self.param_initiate.fundamentals_check(params)
        try:
            financials_url = self.__url_call("fundamentals", "financials")
            financials = requests.get(financials_url, headers=self.headers, params= params)
            if financials.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return financials.json()

    def valuation_ratios(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Valuation Ratios looks at overall financial data like  for a company.

           Arguments:
               Required - company_tickers (str)
               Optional:
                   isin (str) - specifies company data to return.
                   cik (str) - cik identifier
                   date_asof (str) - "YYYY-MM-DD"
           Returns:
               different attributes of the valuation ratios
                       """

        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            valuation_url = self.__url_call("fundamentals", "valuationRatios")
            valuation = requests.get(valuation_url, headers=self.headers, params=params)
            if valuation.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return valuation.json()

    def earning_ratios(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Earning Ratios

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the earning ratios
                              """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            earnings_url = self.__url_call("fundamentals", "earningRatios")
            earnings = requests.get(earnings_url, headers=self.headers, params=params)
            if earnings.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return earnings.json()

    def operation_ratios(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Operation Ratios

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the operation ratios
                              """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            operations_url = self.__url_call("fundamentals", "operationRatios")
            operations = requests.get(operations_url, headers=self.headers, params= params)
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return operations.json()

    def share_class(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Share Class

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the share class.
                                      """

        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            shareclass_url = self.__url_call("fundamentals", "shareClass")
            shareclass = requests.get(shareclass_url, headers=self.headers, params= params)
            if shareclass.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return shareclass.json()

    def earning_reports(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Earning Reports looks at overall earning reports for a company.

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the earning reports.
                                      """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            earningreports_url = self.__url_call("fundamentals", "earningReports")
            earningreports = requests.get(earningreports_url, headers=self.headers, params= params)
            if earningreports.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return earningreports.json()

    def alpha_beta(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Alpha Beta

                  Arguments:
                      Required - company_tickers (str)
                      Optional:
                          isin (str) - specifies company data to return.
                          cik (str) - cik identifier
                          date_asof (str) - "YYYY-MM-DD"
                  Returns:
                      different attributes of the alpha beta.
                                      """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            alphabeta_url = self.__url_call("fundamentals", "alphaBeta")
            alphabeta = requests.get(alphabeta_url, headers=self.headers, params= params)
            if alphabeta.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return alphabeta.json()

    def company_profile(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Company Profile

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the company profile.
                                      """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            companyprofile_url = self.__url_call("fundamentals", "companyProfile")
            company_profile = requests.get(companyprofile_url, headers=self.headers, params= params)
            if company_profile.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return company_profile.json()

    def company(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Company

                      Arguments:
                          Required - company_tickers (str)
                          Optional:
                              isin (str) - specifies company data to return.
                              cik (str) - cik identifier
                              date_asof (str) - "YYYY-MM-DD"
                      Returns:
                          different attributes of the company.
                                              """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            company_url = self.__url_call("fundamentals", "company")
            company = requests.get(company_url, headers=self.headers, params= params)
            if company.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return company.json()

    def share_class_profile_history(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Share Class Profile History

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the share class profile history.
                                              """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            profilehistory_url = self.__url_call("fundamentals", "shareClassProfileHistory")
            profilehistory = requests.get(profilehistory_url, headers=self.headers, params= params)
            if profilehistory.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return profilehistory.json()

    def asset_classification(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Benzinga Asset Classification

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the asset classification.
                                      """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            asset_url = self.__url_call("fundamentals", "assetClassification")
            asset = requests.get(asset_url, headers=self.headers, params= params)
            if asset.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return asset.json()

    def summary(self, company_tickers, isin=None, cik=None, date_asof=None):
        """Public Method: Summary

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      isin (str) - specifies company data to return.
                      cik (str) - cik identifier
                      date_asof (str) - "YYYY-MM-DD"
              Returns:
                  different attributes of the ownership summary.
                                              """
        params = {
            'apikey': self.token,
            "symbols": company_tickers,
            "isin": isin,
            "cik": cik,
            "asOf": date_asof
        }
        self.param_initiate.fundamentals_check(params)
        try:
            summary_url = self.__url_call("ownership", "summary")
            summary = requests.get(summary_url, headers=self.headers, params= params)
            if summary.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return summary.json()

    def ticker_detail(self, company_tickers):
        """Public Method: Ticker detail provides key statistics, peers, and percentile information on the company.

             Arguments:
                 Required - company_tickers (str)

             Returns:
                 Key statistics, peer information and percentile information on the ticker.
                                                     """

        params = {
            "apikey": self.token,
            "symbols": company_tickers
        }
        self.param_initiate.ticker_check(params)
        try:
            ticker_url = self.__url_call("tickerDetail")
            ticker = requests.get(ticker_url, headers=self.headers, params= params)
            if ticker.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return ticker.json()

    def logos(self, company_tickers, filters = None):
        """Public Method: Logos

              Arguments:
                  Required - company_tickers (str)
                  Optional:
                      filters (str) - specifies company data to return.

              Returns:
                  different attributes of the logos
                                              """
        params = {
            "token": self.token,
            "symbols": company_tickers,
            "filters": filters
        }
        self.param_initiate.logos_check(params)
        try:
            logos_url = self.__url_call("logos")
            logos = requests.get(logos_url, headers = self.headers, params=params)
            if logos.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return logos.json()

    def movers(self, session = "REGULAR", period_from = None, period_to = None, max_results = None,
               market_cap_gt = None, close_gt = None, sector = None, market_cap_lt = None):
        """Public Method: Movers Data on Gainers and Losers

              Arguments:
                  Optional:
                      session (str) - "PRE_MARKET, REGULAR, AFTER_MARKET
                      period_from (str) - "YTD" or "-1W" etc.
                      period_to (str) - "YYYY-MM-DD" default is the most recent timestamp
                      max_results (int) - default 10
                      market_cap_gt (str) - market cap greater than "1b" etc
                      market_cap_lt (str) - market cap less than "1b" etc
                      close_gt (str) - close price greater than.
                      sector (str) - sector like "healthcare"


              Returns:
                  different attributes of the gainers and the losers.
                                              """
        if market_cap_gt != None:
            market_cap_greater = ";marketcap_gt_%s" % (market_cap_gt)
        else:
            market_cap_greater = ""
        if market_cap_lt != None:
            marketcap_less = ";marketcap_lt_%s" % (market_cap_lt)
        else:
            marketcap_less = ""
        if close_gt != None:
            close_greater = ";close_gt_%s" % (close_gt)
        else:
            close_greater = ""
        if sector != None:
            sector = ";sector_in_%s" % (sector)
        else:
            sector = ""
        if market_cap_gt == None and market_cap_lt == None and close_gt == None and sector ==None:
            screener_query = None
        else:
            screener_query = "%s%s%s%s"% (market_cap_greater, marketcap_less, close_greater,sector)
        params = {
            "apikey": self.token,
            "from": period_from,
            "to": period_to,
            "session": session,
            "screenerQuery": screener_query,
            "maxResults": max_results
        }
        self.param_initiate.movers_check(params)
        try:
            movers_url = self.__url_call("movers")
            movers = requests.get(movers_url, headers=self.headers, params=params)
            print(movers.url)
            if movers.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return movers.json()

    def output(self, json_object):
        result = json.dumps(json_object, indent= 4)
        return result

test = Benzinga("899efcbfda344e089b23589cbddac62b")
