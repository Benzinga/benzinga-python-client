"benzinga_client.py"
if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    api_key = "22f84f867c5746fd92ef8e13f5835c02"
    newapikey = "54b595f497164e0499409ca93342e394"
    false_token = 0
    company_tickers = "AAPL"
    start_date = "2018-05-01"
    end_date = "2006-09-12"
    sample_run = Benzinga(token)
    test = sample_run.logos()
    sample_run.JSON(test)

"news_api.py"
if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    api_key = "22f84f867c5746fd92ef8e13f5835c02"
    newapikey = "54b595f497164e0499409ca93342e394"
    sample_run = News_API(token)
    test = sample_run.news(pagesize=100, display_output= "full", channel = "Analyst Ratings")
    print(sample_run.JSON(test))

"automated_story.py"
if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    api_key = "22f84f867c5746fd92ef8e13f5835c02"
    newapikey = "54b595f497164e0499409ca93342e394"
    auto = Automate_Movers(token, session= "PRE_MARKET", date_from= "-1y", max_results="5", sector= "healthcare")





