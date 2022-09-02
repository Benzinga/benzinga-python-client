from .benzinga_errors import IncorrectParameterEntry
class Param_Check:

    def __init__(self):
        self.stri = "str"
        self.inte = "int"
        self.nonetype = "NoneType"
        self.float = "float"

    def __para_type_matching(self, param_metadata, para_dict):
        for param, value in para_dict.items():
            if (type(value).__name__ != param_metadata[param]) and (
                type(value).__name__ != self.nonetype
            ):
                raise IncorrectParameterEntry(
                    "Parameter Type for %s doesn't match: Correct Type: %s. "
                    "You entered %s"
                    % (param, param_metadata[param], type(value).__name__)
                )

    def calendar_check(self, dict):
        param_type = {
            'token': self.stri,
            "page": self.inte ,
            "pagesize": self.inte,
            "parameters[date]": self.stri,
            "parameters[date_from]": self.stri,
            "parameters[date_to]": self.stri,
            "parameters[tickers]": self.stri,
            "parameters[importance]": self.inte,
            "parameters[date_sort]": self.stri,
            "parameters[updated]": self.inte,
            "paramaters[dividend_yield_operation]": self.stri,
            "parameters[dividend_yield]": self.float,
            "parameters[action]": self.stri,
            "country": self.stri,
            "parameters[eps_surprise_percent]": self.stri,
            "parameters[revenue_surprise_percent]": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def fundamentals_check(self, dict):
        param_type = {
            'apikey': self.stri,
            "symbols": self.stri,
            "symbol": self.stri,
            "isin": self.stri,
            "cik": self.stri,
            "asOf": self.stri,
            "period": self.stri,
            "reportType": self.stri,
            "token": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def delayed_quote_check(self, dict):
        param_type = {
            'token': self.stri,
            "symbols": self.stri,
            "isin": self.stri,
            "cik": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def logos_check(self, dict):
        param_type = {
            'token': self.stri,
            "symbols": self.stri,
            "filters": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def instruments_check(self, dict):
        param_type = {
            "apikey": self.stri,
            "fields": self.stri,
            "query": self.stri,
            "to": self.stri,
            "from": self.stri,
            "asOf": self.stri,
            "sortfield": self.stri,
            "sortdir": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def security_check(self, dict):
        param_type = {
            "apikey": self.stri,
            "symbol": self.stri,
            "cusip": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def bars_check(self, dict):
        param_type = {
            "token": self.stri,
            "symbols": self.stri,
            "from": self.stri,
            "to": self.stri,
            "interval": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def charts_check(self, dict):
        param_type = {
            "apikey": self.stri,
            "symbol": self.stri,
            "from": self.stri,
            "to": self.stri,
            "interval": self.stri,
            "session": self.stri,
        }
        self.__para_type_matching(param_type, dict)

    def ticker_check(self, dict):
        param_type = {
            "apikey": self.stri,
            "symbols": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def autocomplete_check(self, dict):
        param_type = {
            "token": self.stri,
            "query": self.stri,
            "limit": self.inte,
            "searchMethod": self.stri,
            "exchanges": self.stri,
            "types": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def batchhistory_check(self, dict):
        param_type = {
            "apikey": self.stri,
            "symbol": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def news_check(self, dict):
        param_type = {
            "token": self.stri,
            "pageSize": self.inte,
            "page": self.inte,
            "displayOutput": self.stri,
            "date": self.stri,
            "dateFrom": self.stri,
            "dateTo": self.stri,
            "lastId": self.stri,
            "updatedSince": self.stri,
            "publishedSince": self.stri,
            "tickers": self.stri,
            "channels": self.stri,
            "type": self.stri,
            "limit": self.inte,
            "channel": self.stri
        }
        self.__para_type_matching(param_type, dict)

    def quantified_news_check(self, dict):
        param_type = {
            "token": self.stri,
            "pagesize": self.inte,
            "page": self.inte,
            "date": self.stri,
            "date_from": self.stri,
            "date_to": self.stri,
            "updated_since": self.inte,
            "symbols": self.stri,
            "apikey": self.stri,
        }
        self.__para_type_matching(param_type, dict)

    def movers_check(self, dict):
        param_type = {
            "apikey": self.stri,
            "from": self.stri,
            "to": self.stri,
            "session": self.stri,
            "maxResults": self.stri,
            "screenerQuery": self.stri,
        }
        self.__para_type_matching(param_type, dict)

    def options_check(self, dict):
        param_type = {
            "token": self.stri,
            "page": self.inte,
            "pagesize": self.inte,
            "parameters[date]": self.stri,
            "parameters[date_from]": self.stri,
            "parameters[date_to]": self.stri,
            "parameters[tickers]": self.stri,
            "parameters[updated]": self.inte
        }
        self.__para_type_matching(param_type, dict)
