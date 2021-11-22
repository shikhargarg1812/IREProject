
import json
blogFiles=['../blogs/aleju/aleju.json','../blogs/patrikEmami/patrikEmami.json','../blogs/shagunSogani/shagunSoganiBlog.json','../blogs/shortScience/shortScience.json']
idr=0
finalData={}
for file in blogFiles:
    with open(file) as f:
        jsonObj = json.load(f)
        for idx in jsonObj:
            finalData[str(idr)]=jsonObj[idx]
            idr+=1


jsonObj=json.dumps(finalData,indent=4)
with open('finalData.json','w') as f:
    f.write(jsonObj)

# jsonObj=json.dump(finalData)
# with open()