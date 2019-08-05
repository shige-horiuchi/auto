import time
from selenium import webdriver

ARTICLES = ["Python", "Java", "Ruby", "Haskell"]

driver = webdriver.Chrome()

for article in ARTICLES:
    # Wikipediaのページに遷移
    driver.get("https://ja.wikipedia.org/wiki/" + article)
    driver.find_element_by_css_selector(".infobox").screenshot(article + "_infobox.png")
    time.sleep(5.0)
driver.close()
