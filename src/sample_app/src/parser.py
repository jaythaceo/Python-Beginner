
from bs4 import BeautifulSoup

data_page = open('data_store.html', "r")

content = data_page.read()
soup = BeautifulSoup(content)
links = soup.findAll("a")

new_file = open('newfile.txt', 'w')
new_file.write(links)

data_page.close()
new_file.close()
