import json
import process

rawData = {} 
with open('TwoMinutePapers.json','r') as f:
    rawData = json.load(f)


count_one = 0
count_more = 0
count_zero = 0
for vid in rawData:
    
    vid['source_link'] = 'https://www.youtube.com/watch?v='+vid['video_id']
    link,title = process.get_paperdata(vid['description'])
    if link == '':
        continue
    else:
        vid['paper_link'] = link
        vid['paper_title'] = title
        count_more+=1

print(count_more)
with open('refined_twominpaper.json','w') as f:
    json.dump(rawData,f,indent=4)