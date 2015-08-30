from bs4 import BeautifulSoup
import urllib

url_page = {'page1': 'http://www.utexas.edu/world/univ/alpha/', 'page2': 'http://cohenbanking.com/'}

html_page = urllib.urlopen(url_page['page2']).read()

soup = BeautifulSoup(html_page)

