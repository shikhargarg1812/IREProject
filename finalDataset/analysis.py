import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords

STOPWORDS=stopwords.words('english')
import json
import spacy
from textstat.textstat import textstatistics,legacy_round


file="finalData.json"
jsonObj={}
with open(file) as f:
    jsonObj = json.load(f)
Text=""
for ind in jsonObj:
    Text=Text+jsonObj[ind]['summary']+" "
print(len(Text))
print(len(jsonObj))

text=Text
text=text.split(" ")
text = [t for t in text if t not in STOPWORDS]
text=(" ").join(text)


"""
This function creates the word cloud from the corpus.
"""
def showWorldCloud(text):
    word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def getReadabilityScores():

