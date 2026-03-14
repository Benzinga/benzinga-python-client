![Benzinga Logo](https://raw.githubusercontent.com/Benzinga/benzinga-python-client/master/logo/Benzinga_Logo-navy.png)
# Benzinga's Python Client Library's Documentation

Benzinga's Python client library focuses on financial data methods, that can be used for quantitative analysis, and on news data from Benzinga, that can help give meaningful insights that complement quantitative data.

## Table of Contents
- [Benzinga Python Client](#benzinga-python-client)
  * [Getting Started](#getting-started)
  * [Your Key](#your-key)
  * [Sample Test Financial Data Module](#sample-test-financial-data-module)
  * [Sample Test News Data Module](#sample-test-news-data-module)
  * [Financial Data Methods:](#financial-data-methods-)
    + [Price History](#price-history)
    + [Auto-Complete](#auto-complete)
    + [Security](#security)
    + [Chart](#chart)
    + [Quote](#quote)
    + [Instruments](#instruments)
    + [Dividends](#dividends)
    + [Ratings](#ratings)
    + [Earnings](#earnings)
    + [Splits](#splits)
    + [M&A](#ma)
    + [Economics](#economics)
    + [Guidance](#guidance)
    + [IPO](#ipo)
    + [Retail](#retail)
    + [Conference Calls](#conference-calls)
    + [Fundamentals](#fundamentals)
    + [Financials](#financials)
    + [Valuation Ratios](#valuation-ratios)
    + [Earning Ratios](#earning-ratios)
    + [Operation Ratios](#operation-ratios)
    + [Share Class](#share-class)
    + [Earning Reports](#earning-reports)
    + [Alpha Beta](#alpha-beta)
    + [Company Profile](#company-profile)
    + [Company](#company)
    + [Share Class Profile History](#share-class-profile-history)
    + [Asset Classification](#asset-classification)
    + [Summary](#summary)
    + [Logos](#logos)
    + [Movers](#movers)
    + [Ticker Detail](#ticker-detail)
  * [News Data:](#news-data-)
    + [News](#news)
    + [Top News](#top-news)
    + [Channels](#channels)
    + [Quantified News](#quantified-news)
  * [Additional Links](#additional-links)

## Getting Started

The basic installation instructions are as follows (Recommended):


```shell
pip install git+ssh://git@github.com/Benzinga/benzinga-python-client.git
```

Once you have successfully installed the package, you can either import the
Financial Data module, for quantitative financial data:
```python
from benzingaorg import financial_data
```
or you can import the Benzinga News Data module, if you're looking into financial news:
```python
from benzingaorg import news_data
```

## Your Key

**Api Key** To initiate a class, an API key is used, for
authentication purposes. [Contact us](https://cloud.benzinga.com/lets-talk/) if you don't yet have a key, we will take care of you!

*Sample API Key (type: str) : "testkey892834789s9s8abshtuy"*

## Sample Test Financial Data Module

1. Initiating the class:

```python
from benzingaorg import financial data
api_key = "testkey892834789s9s8abshtuy"
fin = financial_data.Benzinga(api_key)
```

2. A sample test run to get ratings on a stock. (Returns a JSON object):

```python
stock_ratings = fin.ratings()
```

3. Since `fin.ratings()` returns a JSON dict, for a better view of the dict,
you can call the `fin.output()` method on the result. Example:

```python
fin.output(stock_ratings)
```

## Sample Test News Data Module

1. Initiating the class:

```python
from benzingaorg import news_data
api_key = "testkey892834789s9s8abshtuy"
news = news_data.News(api_key)
```

2. A sample test run to get general news. (Returns a JSON Object)

```python
stories = news.news()
```

3. Since `fin.news()` returns a JSON dict, for a better view of the dict,
you can call the `fin.output()` method on the result. Example:

```python
news.output(stories)
```

It is important to note that for both the Financial Data Module and the News Data Module, there are many **Optional** parameters for the methods. Below is a detailed listing of possible methods for the Financial Data Module and the news Data Module, their method
call names, arguments, and what they return.

## Financial Data Methods:

### Price History

```python
fin.price_history()
```
Public Method: Benzinga Price History returns daily candles for a specific date range for a company.
* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Required** - date_from ****(str)**** - "YYYY-MM-DD"
    * **Required** - date_to ****(str)**** - "YYYY-MM-DD"

* Returns:
    * Daily candles for the company for a specific date range


### Auto-Complete

```python
fin.auto_complete()
```

Public Method: Benzinga Auto-Complete returns the relevant information related to a company ticker.
* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * limit ****(int)**** - Limits the number of results to input.
    * search_method ****(str)**** - You can enter either "SYMBOL", which does a prefix match on symbol, or
    "SYMBOL_NAME" which does a prefix match on symbol and prefix match on any word in the name, or
    you can enter "SYMBOL_WITHIN" which matches any part of the symbol.
    * exchanges ****(str)**** - If this value is present, then it will only include those exchanges.
    * types ****(str)**** You can enter either "STOCK", "TYPE" or "OEF".

* Returns:
    * Relevant information such as company name of short name, type and exchange

### Security

```python
fin.security()
```

Public Method: Benzinga Security returns the information regarding the security.
* Arguments:
    * **Required** - company_tickers ****(str)****
        * **Optional**:
        * cusip ****(str)****

* Returns:
    * Symbol, exchange symbol, exchange, country, currency, cusip and description

### Chart

```python
fin.chart()
```

Public Method: Benzinga Chart looks at detailed price values over a period of time.
* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Required** - date_from ****(str)**** For date_from, you can enter "YTD" for the first trading day of the year. "1d", "5d" or "1m". You can also enter the date from in the "YY-MM-DD"format too.
    * **Optional**:
    * date_to ****(str)**** - "YY-MM-DD"
    * interval ****(str)*** -  "1MONTH", "1W", "1D", "1H", "15M". Default: "5M"
    * session ****(str)**** - "ANY", "REGULAR"


* Returns:
    * open, high, low, close, volume, time, dateTime


### Quote

```python
fin.quote()
```

Public Method: Benzinga Quote looks at many different attributes of the ticker like high, low, close etc

* Arguments:
    * **Required** - company_tickers ****(str)****

* Returns:
    *   symbol, dxsymbol, exchange, bzexchange, isoexchange, type, name, description, open
        high, low, close, bid price, ask price, ask size, size, bid time, ask time, last trade price, last
        trade time, volume, change, change percent, previous close price, fifty day average price,
        fifty two week high, fifty two week low, dividend yield, price/earnings, forward price/earnings,
        payout ratio, shares outstanding, open interest, shares per contract, multiplier.

### Instruments

```python
fin.instruments()
```

Public Method: Benzinga Instruments looks at all of the screener data with price statistics, based
         on different attributes.
* Arguments:
    * **Optional**:
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * market_cap_gt ****(str)**** - market cap greater than "1b" etc
    * market_cap_lt ****(str)**** - market cap less than "1b" etc
    * close_gt ****(str)**** - close price greater than.
    * sector ****(str)**** - sector like "healthcare"
    * sort field ****(str)**** - field to sort by (un-tested)
    * sortdir ****(str)**** - direction of sort (un-tested)

* Returns:
    * all of the data related to the instrument including marketcap, sector, company name
         etc, that can be found on the Benzinga Pro screener.

### Dividends

```python
fin.dividends()
```

Public Method: Benzinga Dividends looks at the relevant dividend information for a
         company.

* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on ("ex", "payable", "record")
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    * sort order to be greater or equal to the time stamp indicated.
    * div_yield_operation ****(str)**** - to filter the div yield by for eg. "gt", "gte",
     "eq", "lte", "lt". Not tested
    * div_yield ****(int)**** - div yield amount fo filter by. "1" for 100% or above.

* Returns:
    * the id, date, updated, isin, ticker, name, exchange, frequency, dividend,
     dividend prior, dividend type, dividend yield, ex-dividend date, payable date,
     record date, importance

### Ratings

```python
fin.ratings()
```

Public Method: Benzinga Ratings looks at ratings from different firms

* Arguments:
    * **Optional**:
    * page **(int)** - page offset
    * pagesize **(int)** - limit of results returned
    * date_asof **(str)** - "YYYY-MM-DD"
    * date_from **(str)** - "YYYY-MM-DD"
    * date_to **(str)** - "YYYY-MM-DD"
    * company_tickers **(str)**
    * importance - **(int)** - not tested yet.
    * date_sort - **(str)** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.
    * action - **(str)** - " Upgrades , Downgrades , Maintains , Lowers , Raises ,
    Initiates Coverage On , Terminates Coverage On"

* Returns:
    * id, date, time, ticker, exchange, name, action_pt, action_company, rating_current,
    pt_current, rating_prior, pt_prior, url, importance, updated, url_calendar, url_news,
    analyst, analyst_name

### Earnings

```python
fin.earnings()
```

Public Method: Benzinga Earnings looks at the quarterly earnings reports for different
        companies.

* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
     sort order to be greater or equal to the time stamp indicated.

* Returns:
    * id, date, date confirmed, time, isin, ticker, exchange, name, period, period_year,
    eps, eps_est, eps_prior, eps_surprise, eps_surprise_percent, revenue, revenue est,
    revenue_prior, revenue_surprise, revenue_surprise_percent, importance, updated

### M&A

```python
fin.ma()
```

Public Method: Benzinga Splits looks at the stock splits calendar data

* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.

* Returns:
    * id, updated, date, date_expected, date_completed, acquirer_ticker, acquirer_exchange, 
     acquirer_name, target_ticker, target_exchange, target_name, currency, deal_type, deal_size,
     deal_payment_type, deal_status, deal_terms_extra, importance, notes


### Splits

```python
fin.splits()
```

Public Method: Benzinga Splits looks at the stock splits calendar data

* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.

* Returns:
    * id, updated, date, time, ticker, exchange, importance, ratio, optionable,
     date_ex, date_recorded, date_distribution

### Economics

```python
fin.economics()
```

Public Method: Benzinga Economics looks at different economic events in a country.

* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.
    * country ****(str)**** - 3 digit country code

* Returns:
    * id, date, time, country, event_name, event_period, period_year, actual, actual_t
    consensus, consensus_t, prior, importance, updated, description

### Guidance

```python
fin.guidance()
```

Public Method: Benzinga Guidance looks at different attributes like revenue guidance etc.
* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.
    * country ****(str)**** - 3 digit country code


* Returns:
    * id, date, time, ticker, exchange, name, period, period_year, prelim, eps_guidance_est,
    eps_guidance_max, eps_guidance_min, eps_guidance_prior_max, eps_guidance_prior_min,
    revenue_guidance_est, revenue_guidance_max, revenue_guidance_min, revenue_guidance_prior_max
    , revenue_guidance_prior_min, importance, updated

### IPO

```python
fin.ipo()
```

Public Method: Benzing IPO looks at initial public offering data for companies.
* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.


* Returns:
    * id, date, time, ticker, exchange, name, pricing_date, price_min, price_max, deal_status,
    insider_lockup_days, insider_lockup_date, offering_value, offering_shares, lead_underwriters,
    underwriter_quiet_expiration_days, underwriter_quiet_expiration_date, update

### Retail

```python
fin.retail()
```

Public Method: Benzinga Retail looks at retail data.

* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.


* Returns:
    * id, date, time, ticker, exchange, name, importance, period, period_year, sss,
    sss_est, retail_surprise, updated

### Conference Calls

```python
fin.conference_calls()
```

Public Method: Benzinga Conference calls looks at conference calls.
* Arguments:
    * **Optional**:
    * page ****(int)**** - page offset
    * pagesize ****(int)**** - limit of results returned
    * date_asof ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * company_tickers ****(str)****
    * importance - ****(int)**** - not tested yet.
    * date_sort - ****(str)**** - Dividend date field to sort on
    * updated_params **(int64)** - records last updated unix time stamp. Forces the
    sort order to be greater or equal to the time stamp indicated.
    * country ****(str)**** - 3 digit country code

* Returns:
    * id, date, time, ticker, exchange, name, start_time, phone_num, international_line,
    reservation_num, access_code, webcase_url, importance, updated

### Fundamentals

```python
fin.fundamentals()
```

Public Method: Benzinga Fundamentals looks at overall financial data for a company.

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** "YYYY-MM-DD"

* Returns:
    * company, companyProfile, shareClass, earningReports, financialStatements, operation earning and valuation
     ratios, alphaBeta

### Financials

```python
fin.financials()
```

Public Method: Benzinga Financials looks at overall financial data like  for a company.

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** "YYYY-MM-DD"
    * period ****(str)**** - select from (3M , 6M , 9M , 12M , 1Y)
    * reporttype ****(str)**** - select from (TTM, A (default), R,P)

* Returns:
    * company, financials such as balance sheet information, assets and liabilities


### Valuation Ratios

```python
fin.valuation_ratios()
```

Public Method: Benzinga Valuation Ratios looks at overall financial data like  for a company.

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** "YYYY-MM-DD"


* Returns:
    * different attributes of the valuation ratios

### Earning Ratios

```python
fin.earning_ratios()
```

Public Method: Benzinga Earning Ratios

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** "YYYY-MM-DD"


* Returns:
    * different attributes of the earning ratios

### Operation Ratios

```python
fin.operation_ratios()
```

Public Method: Benzinga Operation Ratios

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of the operation ratios

### Share Class

```python
fin.share_class()
```

Public Method: Benzinga Share Class

* Arguments:
    * **Required** - company_tickers ****(str)****
    * ****Optional****:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of the share class.


### Earning Reports

```python
fin.earning_reports()
```

Public Method: Benzinga Earning Reports looks at overall earning reports for a company.

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of the earning reports.

### Alpha Beta

```python
fin.alpha_beta()
```

Public Method: Benzinga Alpha Beta

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of alphabeta.


### Company Profile

```python
fin.company_profile()
```

Public Method: Benzinga Company Profile

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of company profile.

### Company

```python
fin.company()
```

Public Method: Benzinga Company

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of the company.


### Share Class Profile History

```python
fin.share_class()
```

Public Method: Benzinga Share Class Profile History

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of share class profile history.


### Asset Classification

```python
fin.asset_classification()
```

Public Method: Benzinga Asset Classification

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of the asset classification.

### Summary

```python
fin.summary()
```

Public Method: Summary
* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * isin ****(str)**** - specifies company data to return.
    * cik ****(str)**** - cik identifier
    * date_asof ****(str)**** - "YYYY-MM-DD"

* Returns:
    * different attributes of the summary.


### Logos

```python
fin.logos()
```

Public Method: Benzinga Logos

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * filters ****(str)**** - specifies company data to return.

* Returns:
    * different attributes of the logos

### Movers

```python
fin.movers()
```

Public Method: Movers Data on Gainers and Losers

* Arguments:
    * **Optional**:
    * session ****(str)**** - "PRE_MARKET, REGULAR, AFTER_MARKET
    * period_from ****(str)**** - "YYYY-MM-DD"
    * period_to ****(str)**** - "YYYY-MM-DD" default is the most recent timestamp
    * max_results ******(int)****** - default 10
    * market_cap_gt ****(str)**** - market cap greater than "1b" etc
    * market_cap_lt ****(str)**** - market cap less than "1b" etc
    * close_gt ****(str)**** - close price greater than.
    * sector ****(str)**** - sector like "healthcare"

* Returns:
    * different attributes of the gainers and the losers.

### Ticker Detail

```python
fin.ticker_detail()
```

Public Method: Benzinga Ticker detail provides key statistics, peers, and percentile information on the company.

* Arguments:
    * **Required** - company_tickers ****(str)****

* Returns:
    *  Key statistics, peer information and percentile information on the ticker.

### Options Activity

```python
fin.options_activity()
```
Public Method: Benzinga Options Activity

* Arguments:
    * **Required** - company_tickers ****(str)****
    * **Optional**:
    * pagesize ****(int)**** - Limit is set to 1000
    * page ****(int)****
    * date ****(str)**** - "YYYY-MM-DD"
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"

* Returns:
    * Different attributes for options activity.



## News Data:

```python
fin.news()
```
### News

Public Method: Benzinga News

* Arguments:
    * **Optional**:
    * pagesize ****(int)**** - default is 15
    * page ****(int)**** - default is 0
    * display_output ****(str)**** - select from (full, abstract, headline)
    * base_date ****(str)**** - "YYYY-MM-DD" The date to query for calendar data. Shorthand for date_from and date_to if
      they are the same. Defaults for latest.
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * last_id ****(str)**** - The last ID to start paging from and sorted by and sorted by the last updated date.
    * updated_since ****(str)**** - he last updated unix timestamp (UTC) to pull and sort by.
    * publish_since ****(str)**** - The last publish unix  timestamp (UTC) to pull and sort by.
    * company_tickers ****(str)****
    * channel ****(str)**** - multiple channels separated by comma.

* Returns:
    * Author, created, updated, title, teaser, body, url, image, channels, stocks, tags


### Top News

```python
news.top_news()
```

Public Method: Benzinga Top News

* Arguments:
   * **Optional**:
   * type ****(str)**** - The type of content to select
   * channel ****(str)**** - multiple channels separated by comma.
   * limit ****(str)**** - max period
   * display_output ****(str)**** - select from (full, abstract, headline)

* Returns:
   * Author, created, updated, title, teaser, body, url, image, channels, stocks, tags

### Channels

```python
news.channels()
```

Public Method: Benzinga Channels only focuses on Channel IDs. The below arguments will have no impact
        on what is returned. It is just for reference.

* Arguments:
    * **Optional**:
    * pagesize ****(int)**** - default is 15
    * page ****(int)**** - default is 0
    * display_output ****(str)**** - select from (full, abstract, headline)
    * base_date ****(str)**** - "YYYY-MM-DD" The date to query for calendar data. Shorthand for date_from and date_to if
      they are the same. Defaults for latest.
    * date_from ****(str)**** - "YYYY-MM-DD"
    * date_to ****(str)**** - "YYYY-MM-DD"
    * last_id ****(str)**** - The last ID to start paging from and sorted by and sorted by the last updated date.
    * updated_since ****(str)**** - he last updated unix timestamp (UTC) to pull and sort by.
    * publish_since ****(str)**** - The last publish unix  timestamp (UTC) to pull and sort by.
    * company_tickers ****(str)****
    * channel ****(str)**** - multiple channels separated by comma.

* Returns:
   * Channel name, channel id.

### Quantified News

```python
news.quantified_news()
```

Public Method: Benzinga Quantified News

* Arguments:
   * **Optional**:
   * pagesize ****(int)**** - default is 15
   * page ****(int)**** - default is 0
   * base_date ****(str)**** - "YYYY-MM-DD" The date to query for calendar data. Shorthand for date_from and date_to if
     they are the same. Defaults for latest.
   * date_from ****(str)**** - "YYYY-MM-DD"
   * date_to ****(str)**** - "YYYY-MM-DD"
   * updated_since ****(str)**** - he last updated unix timestamp (UTC) to pull and sort by.
   * publish_since ****(str)**** - The last publish unix  timestamp (UTC) to pull and sort by.

* Returns:
   * multiple attributes like headlines, volume, day open, open gap, range etc.


## Additional Links

* Benzinga News: https://www.benzinga.com/
* Benzinga Pro: https://pro.benzinga.com/
