import financial_data
import news_data

token = input("Enter your API Key:")
company_tickers = "AAPL"
start_date = "2018-05-01"
end_date = "2006-09-12"

"""Sample Run Data Client"""
data = financial_data.Benzinga(token)

"""Sample Run News API"""
news = news_data.News(token)

