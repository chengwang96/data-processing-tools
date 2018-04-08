import urllib
from bs4 import BeautifulSoup


for i in range(111, 601):
    f = open("file1.txt", "a")
    url = "" + str(i)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    soup = str(soup)
    f.write(soup)
    print('save ' + url + '!')
    f.close()

f.close()
