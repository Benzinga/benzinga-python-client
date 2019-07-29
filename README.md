![alt text](https://raw.githubusercontent.com/Benzinga/benzinga-python-client/master/logo/black_logo.png)

# Benzinga Python Client

This is the the official documentation for Benzinga's Python Package. This package
Is compatible with Python v3.x+. For extensive instructions, visit [Benzinga Docs](https://docs.benzinga.io/benzinga-python/)

## Getting Started

The installation process varies depending on your python version and system used. 
The basic installation instructions are as follows:

```shell
pip install benzinga
```

Alternatively, the package can be installed by using:

```shell
pip3 install benzinga
```

Once you have successfully installed the package, you can either import the 
Financial Data module, for quantitative financial data:
```python
from benzinga import financial_data
```
or you can import the Benzinga News Data module, if you're looking into financial news:
```python
from benzinga import news_data
```

## Your Key

**Api Key** To initiate a class, an API key is used, for
authentication purposes. [Contact us](https://cloud.benzinga.com/lets-talk/) if you don't yet have a key, we will take care of you!

*Sample API Key (type: str) : "testkey892834789s9s8abshtuy"*

## Sample Test Financial Data Module 

1. Initiating the class:

```python
from benzinga import financial data
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
from benzinga import news_data
api_key = "testkey892834789s9s8abshtuy"
paper = news_data.News(api_key)
```

2. A sample test run to get general news. (Returns a JSON Object)

```python
stories = paper.news()
```

3. Since `fin.news()` returns a JSON dict, for a better view of the dict,
you can call the `fin.output()` method on the result. Example:

```python
paper.output(stories)
```

It is important to note that for both the Financial Data Module and the News Data Module, there are many **optional** parameters for the methods. Below is a detailed listing of possible methods for the Financial Data Module and the news Data Module, their method call names, arguments, and what they return. 

For more Financial Data and News Data methods, please visit Benzinga Cloud.

## Additional Links

* Benzinga News: https://www.benzinga.com/
* Benzinga Pro: https://pro.benzinga.com/
