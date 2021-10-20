"""
This file extracts the text as well as the links from the url specified as the argument in the command line
"""


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import re

url=sys.argv[1]
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.decompose()


strips = list(soup.stripped_strings)
print("\n".join(strips))




links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print("LINK are *****************************************")
# print(links)
for i in links:
    print(i)