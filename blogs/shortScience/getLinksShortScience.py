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


url="https://shortscience.org/users"
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
    if "user?name=" in link.get('href'):
        if i%2:
            links.append('https://shortscience.org/'+link.get('href'))

print("LINK are *****************************************")
print(links)
for i in links:
    print(i)