# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the Amazon Books website
url = "https://www.amazon.com/s?k=books"

# Make a GET request to the Amazon Books website
response = requests.get(url)

# Parse the response content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the `div` elements with the `class_="s-result-item"` class
products = soup.find_all("div", class_="s-result-item")[:10]

# Create an empty list to store the extracted data
data = []

# Iterate over the `products` variable and extract the title, price, and rating of each product
for product in products:
    title = product.find("a", class_="a-link-normal").text
    price = product.find("span", class_="a-price").text
    rating = product.find("span", class_="a-rating-star").text
    data.append([title, price, rating])

# Create a Pandas DataFrame from the `data` list
df = pd.DataFrame(data, columns=["Title", "Price", "Rating"])

# Save the DataFrame to a CSV file called `products.csv`
df.to_csv("products.csv")
