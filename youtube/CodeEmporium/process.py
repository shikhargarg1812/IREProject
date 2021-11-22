import re

def get_paperdata(text):
    
    # pattern = "📝.*\n.*\n"
    # links_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    # links = re.findall(links_pattern, text)
    # links = re.findall(pattern, text)

    # if len(links) == 0:
    pattern2 = "main paper.*"
    line = re.findall(pattern2, text)
    

    
    paper_link  = ''
    paper_title = ''
    
    if len(line) == 0:
        pattern2 = "Main paper.*"
        line = re.findall(pattern2, text)
        
        if len(line) == 0:
            pattern2 = "Main Paper.*"
            line = re.findall(pattern2, text)
            
            if len(line) == 0:
                paper_link = ''
            else:
                paper_link = line[0]

        else:
            paper_link = line[0]

    else:
        paper_link = line[0]

    if paper_link != '':
        paper_link = paper_link.split(': ')[1]
    
    return paper_link,paper_title