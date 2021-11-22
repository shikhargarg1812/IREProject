import urllib
from urllib.request import Request, urlopen
import urllib
# from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import re

"""
This file extracts the text as well as the links from the url specified as the argument in the command line
"""


url="https://github.com/aleju/papers"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html=urlopen(req).read()

# html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.decompose()

strips = list(soup.stripped_strings)
# print("First is ",strips[0])
# print("\n".join(strips))




links = []
i=0
for link in soup.findAll('a'):
    # print("Links",link)
    i+=1
    # print(link.get('href'))
    if "/aleju/papers/blob/master" in link.get('href'):
        print(link.get('href'))
        links.append('https://github.com/'+link.get('href'))

print("LINK are *****************************************")
print(links)
for i in links:
    print(i)