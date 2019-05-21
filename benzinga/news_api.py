import requests, json
import datetime
from benzinga_errors import (TokenAuthenticationError,RequestAPIEndpointError, IncorrectParameterEntry,
                             URLIncorrectlyFormattedError)
import param_check

class News_API:

    def __init__(self, api_token):
        self.token = api_token
        self.headers = {'accept': 'application/json'}
        self.url_dict = {"API V2": "http://api.benzinga.com/api/v2/"}

        self.__token_check__(self.token)
        self.param_initiate = param_check.Param_Check()

    def __token_check__(self, api_token):
        params = {'token': api_token}
        try:
            sample_url = self.__url_call__("news")
            sample = requests.get(sample_url, headers= self.headers, params=params)
            if sample.status_code == 401:
                raise TokenAuthenticationError
        except TokenAuthenticationError as t:
            print("%sYour token is not valid. Please try again" % (t))

    def __url_call__(self, resource, sub_resource = ""):  # Private Method to modify requests calls
        endpoint_type = {"news": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource),
                         "news-top-stories": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource),
                         "channels": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource),
                         "newsquantified": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource)}

        url_string = endpoint_type[resource]
        return url_string

    def news(self, pagesize = None, page = None, display_output = None, base_date = None,
             date_from = None, date_to = None, last_id = None, updated_since = None,
             publish_since = None, company_tickers = None, channel = None):
        params = {"token": self.token, "pageSize": pagesize, "page": page, "displayOutput": display_output,
        "date": base_date, "dateFrom": date_from, "dateTo": date_to, "lastId": last_id, "updatedSince": updated_since,
        "publishedSince": publish_since, "tickers": company_tickers, "channel": channel}
        self.param_initiate.news_check(params)
        try:
            news_url = self.__url_call__("news")
            news = requests.get(news_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return news.json()

    def top_news(self, pagesize = None, page = None, display_output = None, base_date = None,
                 date_from = None, date_to = None, last_id = None, updated_since = None,
                 publish_since = None, company_tickers = None, channel = None):
        params = {"token": self.token, "pageSize": pagesize, "page": page, "displayOutput": display_output,
                  "date": base_date, "dateFrom": date_from, "dateTo": date_to, "lastId": last_id,
                  "updatedSince": updated_since,
                  "publishedSince": publish_since, "tickers": company_tickers, "channel": channel}
        self.param_initiate.news_check(params)
        try:
            top_news_url = self.__url_call__("news-top-stories")
            top_news = requests.get(top_news_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return top_news.json()

    def channels(self, pagesize=None, page=None, display_output=None, base_date=None,
                 date_from=None, date_to=None, last_id=None, updated_since=None,
                 publish_since=None, company_tickers=None, channel=None):
        params = {"token": self.token, "pageSize": pagesize, "page": page, "displayOutput": display_output,
                  "date": base_date, "dateFrom": date_from, "dateTo": date_to, "lastId": last_id,
                  "updatedSince": updated_since, "publishedSince": publish_since, "tickers": company_tickers,
                  "channel": channel}
        self.param_initiate.news_check(params)
        try:
            channels_url = self.__url_call__("channels")
            channels = requests.get(channels_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return channels.json()

    def quantified_news(self, pagesize=None, page=None, base_date=None, date_from=None,
                        date_to=None, company_tickers = None, updated_since = None):
        params = {"token": self.token, "pagesize": pagesize, "page": page, "date": base_date,
                  "date_from": date_from, "date_to": date_to, "updated_since": updated_since,
                  "symbols": company_tickers}
        self.param_initiate.quantified_news_check(params)
        try:
            quantnews_url = self.__url_call__("newsquantified")
            quantnews = requests.get(quantnews_url, headers=self.headers, params=params)
        except requests.exceptions.RequestException as request_denied:
            print(request_denied)
        return quantnews.json()

    def JSON(self, func_output):
        result = json.dumps(func_output, indent= 4)
        print(result)
        return result

if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    api_key = "22f84f867c5746fd92ef8e13f5835c02"
    newapikey = "54b595f497164e0499409ca93342e394"
    sample_run = News_API(newapikey)
    test = sample_run.news()
    print(sample_run.JSON(test))


