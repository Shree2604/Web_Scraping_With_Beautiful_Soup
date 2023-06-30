# Web Scraping with Beautiful Soup

## Examples

### Scraping the Title

```python
import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    """Scrapes the title of a website."""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    title = soup.title.text
    return title

title = scrape_title('https://www.google.com/')
print(title)
```


### Extraction of URLs

```python
import requests
from bs4 import BeautifulSoup

def scrape_urls(url):
    """Scrapes all of the URLs from a website."""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    urls = soup.find_all('a')
    return urls

urls = scrape_urls('https://www.google.com/')
for url in urls:
    print(url['href'])
```

### Extraction of Paragraphs and Headings

```python
import requests
from bs4 import BeautifulSoup

def scrape_paragraphs_and_headings(url):
    """Scrapes all of the paragraphs and headings from a website."""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    paragraphs = soup.find_all('p')
    headings = soup.find_all('h1', 'h2', 'h3')
    return paragraphs, headings

paragraphs, headings = scrape_paragraphs_and_headings('https://www.google.com/')
for paragraph in paragraphs:
    print(paragraph.text)
for heading in headings:
    print(heading.text)
```

### Extraction of Images

```python
import requests
from bs4 import BeautifulSoup

def scrape_images(url):
    """Scrapes all of the images from a website."""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    images = soup.find_all('img')
    return images

images = scrape_images('https://www.google.com/')
for image in images:
    print(image['src'])
```

### Extraction of Div Tags

```python
import requests
from bs4 import BeautifulSoup

def scrape_div_tags(url):
    """Scrapes all of the div tags from a website."""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    div_tags = soup.find_all('div')
    return div_tags

div_tags = scrape_div_tags('https://www.google.com/')
for div_tag in div_tags:
    print(div_tag)

```
### Extraction of Style 
```python
import requests
from bs4 import BeautifulSoup

def scrape_styles(url):
    """Scrapes all of the styles from a website."""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    styles = soup.find_all('style')
    return styles

styles = scrape_styles('https://www.google.com/')
for style in styles:
    print(style.text)

```

I hope you find these examples helpful!
