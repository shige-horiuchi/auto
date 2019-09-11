from bs4 import BeautifulSoup
import requests

page_data = requests.get('https://commons.wikimedia.org/wiki/Category:Hunting_cats').text
page = BeautifulSoup(page_data, 'lxml')
for img in page.select('.image > img'):
    print(f"見出し： {img.attrs['alt']} URL: {img.attrs['src']}")