import re

def get_paperdata(text):
    
    # pattern = "📝.*\n.*\n"
    # links_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    # links = re.findall(links_pattern, text)
    # links = re.findall(pattern, text)

    # if len(links) == 0:
    # print(text)
    pattern2 = "https://arxiv.org/[^\s\)\]]*[0-9]"
    line = re.findall(pattern2, text)

    
    paper_link  = ''
    paper_title = ''
    
    if len(line) == 0:
        pattern2 = "Paper.*"
        line = re.findall(pattern2, text)
        
        if len(line) != 0:
            if len(line[0].split(': ')) != 1:
                paper_link = line[0].split(': ')[1]

    else:
        paper_link = line[0]
    print(paper_link)

    # if paper_link != '':
    #     paper_link = paper_link.split(': ')[1]
    
    return paper_link,paper_title