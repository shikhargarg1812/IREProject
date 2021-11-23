# IRE Project : Creating a parallel corpus for Layperson Summarization

## Implementation Details:
The link to the source code of implementation is https://github.com/shikhargarg1812/IREProject, below are various sections of our implementation.

### Youtube
In youtube to get raw data we have implemented two methods:-
* Search for playlists by search term automatically and scrape its description, title and transcript. (Present in PlaylistSearch folder in youtube)
* Get a relevant playlist link by manual search and provide it to code to scrape description, transcript and title for all videos. (Present in PlaylistData folder in youtube folder). Using this method, we have scraped data for two playlists present in two files, “CVPR2021.json” and “TwoMinutePapers.json”, inside the youtube directory. 

* We will be finding the mapping of transcripts of videos with paper uniquely. We have implemented this for “Two Minute Papers”, code for this is present in the TwoMinPaper directory inside the youtube directory. This folder also contains the file “refined_twominpaper.json”, which includes the video link, transcript and paper link, title with which video maps.

### Blogs
* The blog folder contains the file “getLinksFromBlog.py”, which extracts all the links from the index page that explains the research papers.

* It also contains four more folders, namely patrikEmam, shagunSogani, Alejo, shortScience, belonging to both extracted blogs, i.e. Shagun Sogani, Patrick Emami,  Aleju, and short Science blogs. 
Additionally, the short Science folder contains all the blogs on the short Science website and not the blog of a single person, as all the blogs on the website contained relevant summaries.

* All the folders contain a python file that extracts the transcripts from the links removed using the “getLinksFromBlog.py” file and extracts the link to the paper, which the blog post explains.

### Arxiv API

* This folder contains two files, “getPaperFromTitle.py” and “getPaperFromXML.py”. The first file extracts the XML from the Arxiv Database from the title provided, the second file “getPaperFromXML.py '', and then pulls the XML file in a JSON format.




## Installation :
Run the following commands to complete installation.
```
pip install urllib3
pip install beautifulsoup4
pip install jsonlib
pip install elementpath
pip install regex
pip install pandas
pip install wordcloud
pip install matplotlib
pip install nltk
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
pip install textstat
```

## Executing the Code:
### For gettting summaries from each of the blog:
Go to the folder corresponding to that blog, in the blogs folder, and run the .py file, this will store all the transcripts in a .json file.

### For analysing the data extracted:
* First merge the data from all the individual files by running 'python3 mergeData.py' in the finalData folder, this will merge all the .json files in the finalData.json file.
* Then to get the word-cloud run 'python3 analysis.py'.
* Then to get the readability scores run 'python3 readability.py'


