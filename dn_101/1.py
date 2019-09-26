import requests
from bs4 import BeautifulSoup

page = requests.get('http://data.gov')
page_bs = BeautifulSoup(page.content, 'html.parser')
a = page_bs.select('small a')[0]
print(a.string[:(-1 * len('datasets'))])
