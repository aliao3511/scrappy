from bs4 import BeautifulSoup
import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2]
print(html.prettify())
body = list(html.children)[3]
print(body.prettify())
p = list(body.children)[1]
print(type(p))
print(p.string)
print(p.get_text())
