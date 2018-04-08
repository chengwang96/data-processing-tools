import urllib
from bs4 import BeautifulSoup
# import re


for i in range(111, 601):
    f = open("file1.txt", "a")
    url = "http://mebook.cc/page/" + str(i)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    # print(soup)
    # content = '<a href="http://mebook.cc/\d*.html" title=".*"><img src=".*.jpg"/>'
    soup = str(soup)
    f.write(soup)
    print('save ' + url + '!')
    f.close()

f.close()
