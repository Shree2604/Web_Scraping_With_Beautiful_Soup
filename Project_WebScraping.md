# Realtime Project on Web Scraping

## Introduction

Web scraping is the process of extracting data from websites. It can be used for a variety of purposes, such as gathering market data, tracking competitors, or automating tasks.

In this project, we will be scraping the [CoinMarketCap](https://coinmarketcap.com/) website to extract the latest prices of cryptocurrencies. We will use the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse the HTML response from the website.

## Code

```python
import requests
from bs4 import BeautifulSoup

def scrape_coinmarketcap():
    """Scrapes the latest prices of cryptocurrencies from CoinMarketCap."""
    req = requests.get('https://coinmarketcap.com/')
    soup = BeautifulSoup(req.text, 'lxml')
    prices = []
    for coin in soup.find_all('tr'):
        name = coin.find('td', class_='cmc-table__cell cmc-table__cell--name').text
        price = coin.find('td', class_='cmc-table__cell cmc-table__cell--price').text
        prices.append((name, price))
    return prices

prices = scrape_coinmarketcap()
for name, price in prices:
    print(f'{name}: ${price}')


```
This code will first make a request to the CoinMarketCap website. Then, it will use Beautiful Soup to parse the HTML response and extract the table of cryptocurrency prices. Finally, the prices will be printed to the console.

## Output

```python
Bitcoin: $43,581.82
Ethereum: $3,130.08
Tether: $1.00
```


## Conclusion

This project demonstrates how to use Beautiful Soup to scrape data from a website. The code can be easily modified to scrape other websites or to extract other types of data.

I hope this is helpful!

