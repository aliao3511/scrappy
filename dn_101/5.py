import requests
from requests.auth import HTTPBasicAuth
import pprint

complaints = requests.get('https://data.consumerfinance.gov/resource/s6ew-h6mp.json',
		    auth=HTTPBasicAuth('33gkdkjs9ufbe02nr0q33lfg0', '5960lgs892qam1swp9on3e6en01vv4t3n9c4pwvmo6ato5v0wi'),
		    params={ '$order': 'date_received', '$limit': '5' }	
		   ).json()
for complaint in complaints:
    pprint.pprint(complaint)
