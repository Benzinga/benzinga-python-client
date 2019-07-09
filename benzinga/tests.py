import financial_data
import news_data

token = "899efcbfda344e089b23589cbddac62b"
api_key = "22f84f867c5746fd92ef8e13f5835c02"
newapikey = "54b595f497164e0499409ca93342e394"


data = financial_data.Benzinga(token)
result = data.ipo()
print(result)

