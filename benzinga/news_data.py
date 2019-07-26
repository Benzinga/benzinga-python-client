import requests, json
from .benzinga_errors import (TokenAuthenticationError,RequestAPIEndpointError, IncorrectParameterEntry,
                             URLIncorrectlyFormattedError, AccessDeniedError)
from .param_check import Param_Check

class News:

    def __init__(self, api_token):
        self.token = api_token
        self.headers = {'accept': 'application/json'}
        self.url_dict = {"API V2": "http://api.benzinga.com/api/v2/"}

        self.__token_check(self.token)
        self.param_initiate = Param_Check()

    def __token_check(self, api_token):
        """Private Method: Token check is a private method that does a basic check for whether the api token has
               access to the fundamentals and/or calendar data. Different tokens have access to different endpoints.
               Disregard the error if your request is fullfilled but the token authentication error is raised.

            Arguments:
                API Token.

            Returns:
                Token authentication error if token is invalid."""
        params = {'token': api_token}
        try:
            sample_url = self.__url_call("news")
            sample = requests.get(sample_url, headers= self.headers, params=params)
            if sample.status_code == 401:
                raise TokenAuthenticationError
        except TokenAuthenticationError as t:
            raise AccessDeniedError

    def __url_call(self, resource, sub_resource=""):
        """Private Method: URL Call is used to take input from the public methods and return the appropriate url format
                for the endpoint. For example, the resource is calendar and the subresource might be ratings. The correct
                url endpoint call is created by using these two.

            Arguments:
                Resource and Sub- Resource

            Returns:
                url for the endpoint call"""
        endpoint_type = {
            "news": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource),
            "news-top-stories": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource),
            "channels": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource),
            "newsquantified": "%s%s/%s" % (self.url_dict["API V2"], resource, sub_resource)
        }
        if resource not in endpoint_type:
            raise URLIncorrectlyFormattedError
        url_string = endpoint_type[resource]
        return url_string

    def news(self, pagesize=None, page=None, display_output=None, base_date=None,
             date_from=None, date_to=None, last_id=None, updated_since=None,
             publish_since=None, company_tickers=None, channel=None):
        """Public Method: Benzinga News

        Arguments:
            Optional:
            pagesize (int) - default is 15
            page (int) - default is 0
            display_output (str) - select from (full, abstract, headline)
            base_date (str) - "YYYY-MM-DD" The date to query for calendar data. Shorthand for date_from and date_to if
            they are the same. Defaults for latest.
            date_from (str) - "YYYY-MM-DD"
            date_to (str) - "YYYY-MM-DD"
            last_id (str) - The last ID to start paging from and sorted by and sorted by the last updated date.
            updated_since (str) - he last updated unix timestamp (UTC) to pull and sort by.
            publish_since (str) - The last publish unix  timestamp (UTC) to pull and sort by.
            company_tickers (str)
            channel (str) - multiple channels separated by comma.

        Returns:
            Author, created, updated, title, teaser, body, url, image, channels, stocks, tags
        """

        params = {
            "token": self.token,
            "pageSize": pagesize,
            "page": page,
            "displayOutput": display_output,
            "date": base_date,
            "dateFrom": date_from,
            "dateTo": date_to,
            "lastId": last_id,
            "updatedSince": updated_since,
            "publishedSince": publish_since,
            "tickers": company_tickers,
            "channels": channel
        }
        self.param_initiate.news_check(params)
        try:
            news_url = self.__url_call("news")
            news = requests.get(news_url, headers=self.headers, params=params)
            if news.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return news.json()

    def top_news(self, display_output=None, channel=None, limit=None, type=None):
        """Public Method: Benzinga Top News

               Arguments:
                   Optional:
                   type (str) - The type of content to select
                   channel (str) - multiple channels separated by comma.
                   limit (str) - max period
                   display_output (str) - select from (full, abstract, headline)

               Returns:
                   Author, created, updated, title, teaser, body, url, image, channels, stocks, tags
               """
        params = {
            "token": self.token,
            "type" : type,
            "displayOutput": display_output,
            "channel": channel,
            "limit": limit
        }
        self.param_initiate.news_check(params)
        try:
            top_news_url = self.__url_call("news-top-stories")
            top_news = requests.get(top_news_url, headers=self.headers, params=params)
            if top_news.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return top_news.json()

    def channels(self, pagesize=None, page=None, display_output=None, base_date=None,
                 date_from=None, date_to=None, last_id=None, updated_since=None,
                 publish_since=None, company_tickers=None, channel=None):
        """Public Method: Benzinga Channels only focuses on Channel IDs. The below arguments will have no impact
        on what is returned. It is just for reference.

               Arguments:
                   Optional:
                   pagesize (int) - default is 15
                   page (int) - default is 0
                   display_output (str) - select from (full, abstract, headline)
                   base_date (str) - "YYYY-MM-DD" The date to query for calendar data. Shorthand for date_from and date_to if
                   they are the same. Defaults for latest.
                   date_from (str) - "YYYY-MM-DD"
                   date_to (str) - "YYYY-MM-DD"
                   last_id (str) - The last ID to start paging from and sorted by and sorted by the last updated date.
                   updated_since (str) - he last updated unix timestamp (UTC) to pull and sort by.
                   publish_since (str) - The last publish unix  timestamp (UTC) to pull and sort by.
                   company_tickers (str)
                   channel (str) - multiple channels separated by comma.

               Returns:
                   Channel name, channel id.

               """
        params = {
            "token": self.token,
            "pageSize": pagesize,
            "page": page,
            "displayOutput": display_output,
            "date": base_date,
            "dateFrom": date_from,
            "dateTo": date_to,
            "lastId": last_id,
            "updatedSince": updated_since,
            "publishedSince": publish_since,
            "tickers": company_tickers,
            "channels": channel
        }
        self.param_initiate.news_check(params)
        try:
            channels_url = self.__url_call("channels")
            channels = requests.get(channels_url, headers=self.headers, params=params)
            if channels.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return channels.json()

    def quantified_news(self, pagesize=None, page=None, base_date=None, date_from=None,
                        date_to=None, company_tickers = None, updated_since = None):
        """Public Method: Benzinga Quantified News

               Arguments:
                   Optional:
                   pagesize (int) - default is 15
                   page (int) - default is 0
                   base_date (str) - "YYYY-MM-DD" The date to query for calendar data. Shorthand for date_from and date_to if
                   they are the same. Defaults for latest.
                   date_from (str) - "YYYY-MM-DD"
                   date_to (str) - "YYYY-MM-DD"
                   updated_since (str) - he last updated unix timestamp (UTC) to pull and sort by.
                   publish_since (str) - The last publish unix  timestamp (UTC) to pull and sort by.

               Returns:
                   multiple attributes like headlines, volume, day open, open gap, range etc.
               """
        params = {
            "token": self.token,
            "pagesize": pagesize,
            "page": page,
            "date": base_date,
            "date_from": date_from,
            "date_to": date_to,
            "updated_since": updated_since,
            "symbols": company_tickers
        }
        self.param_initiate.quantified_news_check(params)
        try:
            quantnews_url = self.__url_call("newsquantified")
            quantnews = requests.get(quantnews_url, headers=self.headers, params=params)
            if quantnews.status_code == 401:
                raise TokenAuthenticationError
        except requests.exceptions.RequestException:
            raise AccessDeniedError
        return quantnews.json()

    def output(self, json_object):
        result = json.dumps(json_object, indent= 4)
        return result

