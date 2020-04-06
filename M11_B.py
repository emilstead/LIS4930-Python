#Module 11_B Assignment
#04-04-2020 
#Emily Milstead

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://www.floridahealth.gov/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html.parser")

for link in soup.find_all ('a'):
	print(link.get('href'))


#Allows time for the site to rest so we are not constantly pulling information from their servers. 
time.sleep(10) khldsfkja
#43200- seconds in 12 hours
