from bs4 import BeautifulSoup
import urllib

url_page = { "page1": "https://en.wikipedia.org/wiki/United_States_presidential_election,_2016"}

html_page = urllib.urlopen(url_page['page1']).read()

soup = BeautifulSoup(html_page)
links = soup.findAll("a")

for i in links:
  changer = i


changer = str(links)
files = open("newfile.txt", "w")
files.write(changer)
files.close()