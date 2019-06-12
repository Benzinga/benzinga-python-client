import financial_data
import news_data

token = "899efcbfda344e089b23589cbddac62b"
api_key = "22f84f867c5746fd92ef8e13f5835c02"
newapikey = "54b595f497164e0499409ca93342e394"

company_tickers = "AAPL"
start_date = "2018-05-01"
end_date = "2006-09-12"

"""Sample Run Data Client"""
data = financial_data.Benzinga(token)

"""Sample Run News API"""
news = news_data.News(token)

print(data.output(data.movers(session = "REGULAR", sector = "healthcare", max_results = "100", interval= "YTD")))