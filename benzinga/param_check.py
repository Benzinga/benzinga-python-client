from benzinga_errors import (TokenAuthenticationError, RequestAPIEndpointError, IncorrectParameterEntry,
                             URLIncorrectlyFormattedError)
class Param_Check:

    def __init__(self):
        self.stri = "str"
        self.inte = "int"
        self.nonetype = "NoneType"

    def __para_type_matching__(self, param_metadata, para_dict):
        for param, value in para_dict.items():
            try:
                if (type(value).__name__ != param_metadata[param]) and (type(value).__name__ != self.nonetype) :
                    raise IncorrectParameterEntry("Parameter Type for %s doesn't match: Correct Type: %s. "\
                                                  "You entered %s" %
                                                  (param, param_metadata[param], type(value).__name__ ))
            except IncorrectParameterEntry as e:
                print(e)

    def calendar_check(self, dict):
        param_type = {'token': self.stri, "page": self.inte , "pagesize": self.inte, "parameters[date]": self.stri,
                  "parameters[date_from]": self.stri, "parameters[date_to]": self.stri, "parameters[tickers]"
                  :self.stri, "parameters[importance]": self.inte, "parameters[date_sort]": self.stri,
                  "parameters[updated]": self.inte, "paramaters[dividend_yield_operation]": self.stri,
                  "parameters[dividend_yield]": self.stri, "parameters[action]": self.stri, "country": self.stri,
                    "parameters[eps_surprise_percent]": self.stri, "parameters[revenue_surprise_percent]": self.stri}
        self.__para_type_matching__(param_type, dict)

    def fundamentals_check(self, dict):
        param_type = {'token': self.stri, "symbols": self.stri, "symbol": self.stri, "isin": self.stri, "cik": self.stri, "asOf": self.stri,
                  "period": self.stri, "reportType": self.stri}
        self.__para_type_matching__(param_type, dict)


    def delayed_quote_check(self, dict):
        param_type = {'token': self.stri, "symbols": self.stri, "isin": self.stri, "cik": self.stri}
        self.__para_type_matching__(param_type, dict)

    def logos_check(self, dict):
        param_type = {'token': self.stri, "symbols": self.stri, "filters": self.stri}
        self.__para_type_matching__(param_type, dict)

    def instruments_check(self, dict):
        param_type = {"token": self.stri, "fields": self.stri, "query": self.stri, "start_date": self.stri,
                  "date_from": self.stri, "date_to": self.stri, "date_asof": self.stri, "sortfield": self.stri,
                  "sortdir": self.stri}
        self.__para_type_matching__(param_type, dict)

    def security_check(self, dict):
        param_type = {"apikey": self.stri, "symbol": self.stri, "cusip": self.stri}
        self.__para_type_matching__(param_type, dict)

    def autocomplete_check(self, dict):
        param_type = {"token": self.stri, "query": self.stri, "limit": self.inte, "searchMethod": self.stri,
                      "exchanges": self.stri, "types": self.stri}
        self.__para_type_matching__(param_type, dict)

    def batchhistory_check(self, dict):
        param_type = {"apikey": self.stri, "symbol": self.stri}
        self.__para_type_matching__(param_type, dict)

    def news_check(self, dict):
        param_type = {"token": self.stri, "pageSize": self.inte, "page": self.inte, "displayOutput": self.stri,
                  "date": self.stri, "dateFrom": self.stri, "dateTo": self.stri, "lastId": self.stri,
                  "updatedSince": self.stri, "publishedSince": self.stri, "tickers": self.stri, "channel": self.stri}
        self.__para_type_matching__(param_type, dict)

    def quantified_news_check(self, dict):
        param_type = {"token": self.stri, "pagesize": self.inte, "page": self.inte, "date": self.stri,
                      "date_from": self.stri, "date_to": self.stri, "updated_since": self.inte, "symbols": self.stri}
        self.__para_type_matching__(param_type, dict)












