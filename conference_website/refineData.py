import json
file="nips_2019.json"
newObj=[]
with open(file) as f:
    jsonObj = json.load(f)
    # arr=['paper_link','']
    for data in jsonObj:
        newData={}
        newData['sourceUrl']=data['video_link']
        newData['sourceType']='Conference'
        newData['linkToPaper']=data['paper_pdf_link']
        newData['summary']=data['transcript']
        if newData['summary']!='NA':
            newObj.append(newData)
jsonObj=json.dumps(newObj,indent=4)
with open('refined_nips_2019.json','w') as f:
    f.write(jsonObj)


