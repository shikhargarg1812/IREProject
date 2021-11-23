
import json
blogFiles=['../blogs/aleju/aleju.json','../blogs/patrikEmami/patrikEmami.json','../blogs/shagunSogani/shagunSoganiBlog.json','../blogs/shortScience/shortScience.json']
idr=0
finalData={}
for file in blogFiles:
    with open(file) as f:
        jsonObj = json.load(f)
        for idx in jsonObj:
            if('transcript' not in jsonObj[idx]):

                print("FileName",file,idx)
                break
            jsonObj[idx]['summary']=jsonObj[idx]['transcript']
            jsonObj[idx].pop('transcript')
            finalData[str(idr)]=jsonObj[idx]
            idr+=1

youtubeFiles=['../youtube/CodeEmporium/refined_codeemporium.json','../youtube/TwoMinPaper/refined_twominpaper.json','../youtube/YannicKil/refined_yannickil.json','../conference_website/refined_nips_2019.json']
for file in youtubeFiles:
    with open(file) as f:
        jsonObj = json.load(f)
        for data in jsonObj:
            finalData[str(idr)]=data
            idr+=1
            # if 'trans'
jsonObj=json.dumps(finalData,indent=4)
with open('finalData.json','w') as f:
    f.write(jsonObj)
