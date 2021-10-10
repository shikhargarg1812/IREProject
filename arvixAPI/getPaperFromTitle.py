"""
This file extracts the file from the title
"""
import urllib.request as libreq
import re
title="Impact of Electron-Electron Cusp on Configuration Interaction Energies"
title=re.split(' |-',title)
query=""
for i in range(len(title)):
    query+=title[i]
    if i == 0:
        query+='+'
    elif i!=0 and i!=len(title)-1:
        query+='+AND+'
query+=')'
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=ti:('+query) as url:
    r = url.read()
    r=r.decode("utf-8")
with open('temp','w') as f:
    f.write(r)

# print(r)
