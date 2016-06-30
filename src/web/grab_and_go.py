"""
campaign finance 

"""
from bs4 import BeautifulSoup
import requests

url = requests.get('http://docquery.fec.gov/cgi-bin/forms/C00580100/1079423/sb/ALL/3')

data = url.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
	print(link.get('href'))
