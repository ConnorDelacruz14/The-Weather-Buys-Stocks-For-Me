import requests
from bs4 import BeautifulSoup

#empty stock list
stock_list = []

result = requests.get('https://finance.yahoo.com/lookup/')
src = result.content
soup = BeautifulSoup(src, 'lxml')

soup = soup.find("tbody")

for a in soup.find_all('a', href=True):
    stock_list.append(a.text)
