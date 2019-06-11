![alt text](https://14bis.aero/wp-content/uploads/2018/05/benzinga-logo-300x104.png)

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
authentication purposes. Don't worry! We'll provide you with the API Key.

*Sample API Key (type: str) : test123api878key892aksk762ks2e12*

## Sample Test Financial Data Module 

1. Initiating the class:

```python
from benzinga import financial data
api_key = "test123api878key892aksk762ks2e12"
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
api_key = "test123api878key892aksk762ks2e12"
paper = news_data.News(api_key)
```

2. A sample test run to get general news. (Returns a JSON Object)

```python
stories = paper.news()
```

3. Since `paper.news()` returns a JSON dict, for a better view of the dict,
you can call the `paper.output()` method on the result. Example:

```python
paper.output(stories)
```

## Additional Links

* Benzinga API Documentation: https://docs.benzinga.io/benzinga/
* Benzinga News: https://www.benzinga.com/
* Benzinga Pro: https://pro.benzinga.com/

## License

[MIT License](http://opensource.org/licenses/MIT)









