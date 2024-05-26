import requests
from bs4 import BeautifulSoup

url = "https://dominopizza.ru/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser") 
zakuski = soup.find('div', id="zakuski", class_="products-grid-item")
zakuski_data = zakuski.find_all('div', class_ = 'col')


for i in zakuski_data: 
    name = i.find('div', class_="product-name").text.strip()
    namme = i.find('div', class_="description-container").text.strip()
    price = i.find('div', class_='price').text
    url_img = i.find("img").get("src")
    print('----------------------------------------------------------')
    print(name + "\n" + namme + "\n" + price + "\n" + url_img + "\n\n")
    print('----------------------------------------------------------')


