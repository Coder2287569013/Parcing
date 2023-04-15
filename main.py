import requests
from bs4 import BeautifulSoup

pages = []
url = f"https://scrapingclub.com/exercise/list_basic"
responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')
am_pages = soup.find_all("li", class_='page-item')
for page in am_pages:
    pages.append(page.text)
for i in range(len(pages)):
    url = f"https://scrapingclub.com/exercise/list_basic/?page={i+1}"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    quotes = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for quote in quotes:
        print(quote.text)