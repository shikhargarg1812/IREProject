import json
import process

rawData = {} 
with open('YannicKil.json','r') as f:
    rawData = json.load(f)


count_one = 0
count_more = 0
count_zero = 0

finalData = []
for vid in rawData:
    oneData = {}
    oneData['sourceUrl'] = 'https://www.youtube.com/watch?v='+vid['video_id']
    oneData['summary'] = vid['description']
    link,title = process.get_paperdata(vid['description'])
    if link == '':
        continue
    else:
        oneData['sourceType'] = 'youtube'
        oneData['linkToPaper'] = link
        count_more+=1
    finalData.append(oneData)

print(count_more)
with open('refined_yannickil.json','w') as f:
    json.dump(finalData,f,indent=4)