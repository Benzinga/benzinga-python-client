import benzinga_client
import news_api
import json
token = "899efcbfda344e089b23589cbddac62b"
api_key = "22f84f867c5746fd92ef8e13f5835c02"
newapikey = "54b595f497164e0499409ca93342e394"
company_tickers = "AAPL"
start_date = "2018-05-01"
end_date = "2006-09-12"

"""Sample Run Data Client"""
data = benzinga_client.Benzinga(token)
data_output = json.dumps(data.logos(company_tickers=company_tickers), indent=4)


"""Sample Run News API"""
news = news_api.News(token)
output = json.dumps(news.channels(), indent=4)
print(output)
