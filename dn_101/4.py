import requests
import pprint

api_key = 'mAeURNuEP02sWcsJetZ4kcIs4lhpasvZaVH5ouAbLqo='

# codelist = requests.get('https://data.usajobs.gov/api/codelist/occupationalseries').json()
# pprint.pprint(codelist)
lib_code = 1400

page = requests.get('https://data.usajobs.gov/api/search', 
		     params={ 'JobCategoryCode': lib_code },
	             headers={ 'Authorization-Key': api_key },
		   )
pprint.pprint(page.json()['SearchResult']['SearchResultCountAll'])
