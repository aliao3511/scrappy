import requests
from bs4 import BeautifulSoup

page = requests.get('https://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
page_bs = BeautifulSoup(page.content, 'html.parser')
h3 = page_bs.select('h3.dataset-heading')[0]
a = list(h3.children)[1]
print(a.string.strip())
