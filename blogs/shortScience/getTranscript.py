import urllib
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import sys
import re
import json

urls=['https://shortscience.org/user?name=karpathy', 'https://shortscience.org/user?name=hlarochelle', 'https://shortscience.org/user?name=qureai', 'https://shortscience.org/user?name=marvinteichmann', 'https://shortscience.org/user?name=sarath', 'https://shortscience.org/user?name=jgauthier', 'https://shortscience.org/user?name=nandinics', 'https://shortscience.org/user?name=kdubovikov', 'https://shortscience.org/user?name=fabianboth', 'https://shortscience.org/user?name=mcaccia', 'https://shortscience.org/user?name=evgeniizh', 'https://shortscience.org/user?name=abhigenie92', 'https://shortscience.org/user?name=gandhivivek9', 'https://shortscience.org/user?name=felipe', 'https://shortscience.org/user?name=odakyildiz', 'https://shortscience.org/user?name=pemami4911', 'https://shortscience.org/user?name=unmesh', 'https://shortscience.org/user?name=nishnik', 'https://shortscience.org/user?name=josesotelo', 'https://shortscience.org/user?name=prateekgupta', 'https://shortscience.org/user?name=andreaw', 'https://shortscience.org/user?name=fabioperez', 'https://shortscience.org/user?name=nandini', 'https://shortscience.org/user?name=jeremypinto', 'https://shortscience.org/user?name=ukrdailo', 'https://shortscience.org/user?name=abhishm', 'https://shortscience.org/user?name=razah', 'https://shortscience.org/user?name=fweberling1995', 'https://shortscience.org/user?name=robertmueller', 'https://shortscience.org/user?name=adamoyoung', 'https://shortscience.org/user?name=cw', 'https://shortscience.org/user?name=soja', 'https://shortscience.org/user?name=devin132', 'https://shortscience.org/user?name=janrocketman', 'https://shortscience.org/user?name=dav1309', 'https://shortscience.org/user?name=weidai', 'https://shortscience.org/user?name=dniku', 'https://shortscience.org/user?name=ankeshanand', 'https://shortscience.org/user?name=richardwth', 'https://shortscience.org/user?name=niektax', 'https://shortscience.org/user?name=mnoukhov', 'https://shortscience.org/user?name=pavansettigunte', 'https://shortscience.org/user?name=saeedizadi', 'https://shortscience.org/user?name=boucherg', 'https://shortscience.org/user?name=jwturner', 'https://shortscience.org/user?name=natalia', 'https://shortscience.org/user?name=robromijnders', 'https://shortscience.org/user?name=spio', 'https://shortscience.org/user?name=tqri', 'https://shortscience.org/user?name=mrdrozdov', 'https://shortscience.org/user?name=cyberplasm', 'https://shortscience.org/user?name=kundan2510', 'https://shortscience.org/user?name=yoshua', 'https://shortscience.org/user?name=yangjunpro', 'https://shortscience.org/user?name=beahacker', 'https://shortscience.org/user?name=udibr', 'https://shortscience.org/user?name=decodyng', 'https://shortscience.org/user?name=gngdb', 'https://shortscience.org/user?name=shagunsodhani', 'https://shortscience.org/user?name=hbertrand', 'https://shortscience.org/user?name=dasabir', 'https://shortscience.org/user?name=davidstutz', 'https://shortscience.org/user?name=ameroyer', 'https://shortscience.org/user?name=apoorvashetty', 'https://shortscience.org/user?name=martinthoma', 'https://shortscience.org/user?name=anirudhnj', 'https://shortscience.org/user?name=ryandsouza', 'https://shortscience.org/user?name=mashayekhi', 'https://shortscience.org/user?name=wassname', 'https://shortscience.org/user?name=elbaro', 'https://shortscience.org/user?name=tiagotvv', 'https://shortscience.org/user?name=henryzlo', 'https://shortscience.org/user?name=abhshkdz', 'https://shortscience.org/user?name=petered', 'https://shortscience.org/user?name=kirillpe', 'https://shortscience.org/user?name=artems', 'https://shortscience.org/user?name=ofirpress', 'https://shortscience.org/user?name=dennybritz', 'https://shortscience.org/user?name=aleju', 'https://shortscience.org/user?name=joecohen', 'https://shortscience.org/user?name=jyang772', 'https://shortscience.org/user?name=darel', 'https://shortscience.org/user?name=inference', 'https://shortscience.org/user?name=sina', 'https://shortscience.org/user?name=duchaaiki', 'https://shortscience.org/user?name=cdmurray80', 'https://shortscience.org/user?name=muntermulehitch', 'https://shortscience.org/user?name=marek', 'https://shortscience.org/user?name=michaelmmeskhi', 'https://shortscience.org/user?name=felipemartins', 'https://shortscience.org/user?name=hanochkremer', 'https://shortscience.org/user?name=desiananurchalifah', 'https://shortscience.org/user?name=sudharsansai', 'https://shortscience.org/user?name=kakumarabhishek', 'https://shortscience.org/user?name=gkcalat', 'https://shortscience.org/user?name=capybaralet', 'https://shortscience.org/user?name=gabriel', 'https://shortscience.org/user?name=raghu', 'https://shortscience.org/user?name=krishnamurthy', 'https://shortscience.org/user?name=daisy', 'https://shortscience.org/user?name=anmolsharma', 'https://shortscience.org/user?name=tessberthier', 'https://shortscience.org/user?name=benbogin', 'https://shortscience.org/user?name=sepandhaghighi', 'https://shortscience.org/user?name=kkalipcioglu', 'https://shortscience.org/user?name=florianwindolf', 'https://shortscience.org/user?name=royi', 'https://shortscience.org/user?name=txzhao', 'https://shortscience.org/user?name=arshamg', 'https://shortscience.org/user?name=inoryy', 'https://shortscience.org/user?name=mweiss', 'https://shortscience.org/user?name=arjoonn', 'https://shortscience.org/user?name=luyuchen', 'https://shortscience.org/user?name=arian', 'https://shortscience.org/user?name=biedenka', 'https://shortscience.org/user?name=bradyneal', 'https://shortscience.org/user?name=tom89', 'https://shortscience.org/user?name=isarandi', 'https://shortscience.org/user?name=mavenlin', 'https://shortscience.org/user?name=mihail911', 'https://shortscience.org/user?name=azaidi93', 'https://shortscience.org/user?name=langusta', 'https://shortscience.org/user?name=mathieuseurin', 'https://shortscience.org/user?name=yenchenlin', 'https://shortscience.org/user?name=cubs', 'https://shortscience.org/user?name=sam', 'https://shortscience.org/user?name=neeti', 'https://shortscience.org/user?name=tmills', 'https://shortscience.org/user?name=rayraycano', 'https://shortscience.org/user?name=kyunghyuncho', 'https://shortscience.org/user?name=loeh', 'https://shortscience.org/user?name=yzsos', 'https://shortscience.org/user?name=dave31415', 'https://shortscience.org/user?name=niz', 'https://shortscience.org/user?name=csaba', 'https://shortscience.org/user?name=fartash', 'https://shortscience.org/user?name=n0mad', 'https://shortscience.org/user?name=nunocgarcia', 'https://shortscience.org/user?name=liewjunhao', 'https://shortscience.org/user?name=zhewei', 'https://shortscience.org/user?name=astrobites', 'https://shortscience.org/user?name=beomjoonkim', 'https://shortscience.org/user?name=shanexia', 'https://shortscience.org/user?name=twominutepapers', 'https://shortscience.org/user?name=gessulat', 'https://shortscience.org/user?name=semaphore', 'https://shortscience.org/user?name=yongzhuang', 'https://shortscience.org/user?name=kyle', 'https://shortscience.org/user?name=yahui', 'https://shortscience.org/user?name=malmeida', 'https://shortscience.org/user?name=hoqqanen', 'https://shortscience.org/user?name=attar', 'https://shortscience.org/user?name=mwhittaker', 'https://shortscience.org/user?name=eddiesmolansky', 'https://shortscience.org/user?name=evansu', 'https://shortscience.org/user?name=openreview', 'https://shortscience.org/user?name=leopaillier', 'https://shortscience.org/user?name=kangchenghou', 'https://shortscience.org/user?name=acawiki', 'https://shortscience.org/user?name=nipsreviews', 'https://shortscience.org/user?name=zhao', 'https://shortscience.org/user?name=borgr', 'https://shortscience.org/user?name=guillaumechevalier', 'https://shortscience.org/user?name=daisystanton', 'https://shortscience.org/user?name=dawei', 'https://shortscience.org/user?name=zemblan', 'https://shortscience.org/user?name=scottherford', 'https://shortscience.org/user?name=sudoyan', 'https://shortscience.org/user?name=esparami']
data={}
ind=0

for url in urls:
    if ind % 10 ==0:
        print(ind)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html=urlopen(req).read()

    soup = BeautifulSoup(html)

    prevToPrev=""
    links=""
    linkToPaper=""
    prevLink=""
    temp="source panel-body entry"
    linkRoot="https://shortscience.org/"
    for link in soup.findAll(True):
        tempData={}
        # linkToPost=""
        if link.name == "a" and link.text==" scholar.google.com":
            linkToPaper=prevLink
        if link.name == "a":
            prevLink=link.get('href')
        if link.name=="a" and link.has_attr('href') and './paper' in link.get('href'):
            # print()
            linkToPost=linkRoot+ link.get('href')[2:]
        if link.has_attr('class') and 'source' in link.get('class'):
            tempData['sourceUrl']=linkToPost
            tempData['transcript']=link.text
            tempData['sourceType']='blog'
            tempData['linkToPaper']=linkToPaper
            data[str(ind)]=tempData
            ind+=1
        if link.has_attr('class') and 'papertile' in link.get('class'):
            print("*****")
            print(link.text)

    # userName=url.split('=')[1]
jsonObj=json.dumps(data,indent=4)
with open('shortScience.json','w') as f:
    f.write(jsonObj)
