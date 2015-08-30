from bs4 import BeautifulSoup
import urllib

url_page = { "page1": "https://en.wikipedia.org/wiki/United_States_presidential_election,_2016"}

html_page = urllib.urlopen(url_page['page1']).read()

soup = BeautifulSoup(html_page)
links = soup.findAll("a")
data_store = open('data_store.html', "w")

data_store.write(html_page)
data_store.close()
