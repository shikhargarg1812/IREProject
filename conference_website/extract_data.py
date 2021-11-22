

import urllib
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import sys
import re
import json
import requests
import pandas as pd
from collections import defaultdict

URL = "https://nips.cc/Conferences/2019/Videos"
data = defaultdict(list)

r = requests.get(URL)
html = r.text

p =  'http://papers\\.nips\\.cc/paper/by\\-source\\-2019-.*\\"'
paper_links = [item.split('"')[0] for item in re.findall(p, html)]


p = '<div class="maincardBody">.*</div>'
paper_titles = [item.split('>')[1].split('<')[0] for item in re.findall(p, html)]

p = '<div class="maincardFooter">.*</div>'
paper_authors = [item.split('>')[1].split('<')[0] for item in re.findall(p, html)]

p = '<p class="abstract".*</p>'
abstracts = [item.split('>')[1].split('<')[0] for item in re.findall(p, html)]

p = '.*3 min Video.*'
video_links = [item.split('"')[1] for item in re.findall(p, html)]


paper_pdf_links = []
for item in paper_links:
    try:
        r =   requests.head(item, allow_redirects=True)
        url =  r.url.replace("/hash/", "/file/").replace("Abstract.html", "Paper.pdf")
    except:
        url = "NA"
    paper_pdf_links.append(url)

data = {
"paper_titles": paper_titles,
"paper_links": paper_links,
"paper_pdf_links": paper_pdf_links,
"paper_authors": paper_authors,
"abstracts": abstracts,
"video_links": video_links,
}

df = pd.DataFrame(data)

df.to_csv("nips_2019.csv", index=None)