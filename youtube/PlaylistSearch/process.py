import re

def get_paperdata(text):
    
    # pattern = "📝.*\n.*\n"
    # links_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    # links = re.findall(links_pattern, text)
    # links = re.findall(pattern, text)

    # if len(links) == 0:
    pattern2 = "The paper.*\"[\s\S]*\".*\n.*\n"
    line = re.findall(pattern2, text)
    
    paper_link  = ''
    paper_title = ''
    
    if len(line) == 1:
        # print('\n',line[0])

        if len(line[0].split('https')) > 1:
            paper_link = 'https'+line[0].split('https')[1].strip()
        else:
            paper_link = 'http'+line[0].split('http')[1].strip()
        
        if len(line[0].split('"')) > 1:
            paper_title = line[0].split('"')[1]
        else:
            paper_title = line[0].split('\'')[1]
    # else:
    #     print(text)
    #     print(line)
    
    return paper_link,paper_title