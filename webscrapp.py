import requests
from bs4 import BeautifulSoup

def get_flipkart_price(product_name):
    url = f"https://www.flipkart.com/search?q={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product = soup.find('div', {'class': '_4rR01T'})
    price = soup.find('div', {'class': '_30jeq3'})
    if product and price:
        return product.text, price.text
    else:
        return None, None

def get_amazon_price(product_name):
    url = f"https://www.amazon.in/s?k={product_name}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    product = soup.find('span', {'class': 'a-size-medium'})
    price = soup.find('span', {'class': 'a-price-whole'})
    if product and price:
        return product.text.strip(), price.text.strip()
    else:
        return None, None

def compare_prices(product_name):
    flipkart_product, flipkart_price = get_flipkart_price(product_name)
    amazon_product, amazon_price = get_amazon_price(product_name)

    if flipkart_product and flipkart_price:
        print("Flipkart - Product:", flipkart_product, "| Price:", flipkart_price)
    else:
        print("Flipkart - Product not found")

    if amazon_product and amazon_price:
        print("Amazon - Product:", amazon_product, "| Price:", amazon_price)
    else:
        print("Amazon - Product not found")

# Example usage
product_name = input("Enter the product name to compare prices: ")
compare_prices(product_name)