import requests, json
from .benzinga_errors import (AccessDeniedError, TokenAuthenticationError, URLIncorrectlyFormattedError,
                              RateLimitError, ServiceUnavailableError, PreconditionFailedError, NotFoundError,
                              BadRequestError, GatewayTimeoutError)
from .param_check import Param_Check
from .config import requests_retry_session
import structlog

log = structlog.get_logger()


class News:

    def __init__(self, api_token, log=True):
        self.token = api_token
        self.headers = {'accept': 'application/json'}
        self.url_dict = {"API V2": "http://api.benzinga.com/api/v2/"}

        self.__token_check(self.token)
        self.param_initiate = Param_Check()
        self.log = log

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
            sample = requests_retry_session().get(sample_url, headers=self.headers, params=params, timeout=10)
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

    def __check_status(self, status_code):
        if status_code == 400:
            raise BadRequestError
        if status_code == 401:
            raise TokenAuthenticationError
        elif status_code == 403:
            raise TokenAuthenticationError
        elif status_code == 404:
            raise NotFoundError
        elif status_code == 412:
            raise PreconditionFailedError
        elif status_code == 429:
            raise RateLimitError
        elif status_code == 500:
            raise ServiceUnavailableError
        elif status_code == 502:
            raise ServiceUnavailableError
        elif status_code == 503:
            raise ServiceUnavailableError
        elif status_code == 504:
            raise GatewayTimeoutError

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
            news = requests_retry_session().get(news_url, headers=self.headers, params=params, timeout=10)
            statement = "Status Code: {status_code} Endpoint: {endpoint}".format(endpoint=news.url,
                                                                                 status_code=news.status_code)
            if self.log:
                log.info(statement)
            self.__check_status(news.status_code)
        except requests.exceptions.RequestException as err:
            self.__check_status(err.response.status_code)
        return news.json()
