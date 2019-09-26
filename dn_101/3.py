import requests

page = requests.get('https://analytics.usa.gov/data/live/ie.json').json()
print(page['totals']['ie_version']['6.0'])

