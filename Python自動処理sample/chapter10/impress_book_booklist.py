from bs4 import BeautifulSoup
import requests
page_data = requests.get('https://book.impress.co.jp/booklist/').text
page = BeautifulSoup(page_data, 'lxml')
books = page.select("""
body > div.block-wrap > div.block-content > main > div > div.block-book-list.module-img-s > div.block-book-list-body > div > div > div > div > div.module-book-list-item-body > div.module-book-list-item-body-head > h4 > a
""")
for book in books:
    print(f'タイトル: {book.text}')
    print(f'URL: {book.get("href")}')
