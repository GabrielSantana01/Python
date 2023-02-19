import urllib.request
from bs4 import BeautifulSoup

wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page, 'html5lib')
list_item = soup.title
list_item2 = soup.title.string
list_item3 = soup.find_all('a')
list_item4 = soup.find_all('a')
for link in list_item4:
    print(link.get('href'))
"list_item = soup.find('li', attrs={'class': 'sidebar-toc-list-item sidebar-toc-level-2'})"
'name = list_item.text.strip()'
print(list_item)
print(list_item2)
print(list_item3)
'print(soup.prettify())'
