import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
links=['https://pemami4911.github.io/paper-summaries/deep-rl/2018/09/13/addressing-challenges-in-deep-rl.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2017/05/31/recurrent-environment-simulators.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/12/20/learning-to-navigate-in-complex-envs.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/10/08/unifying-count-based-exploration-and-intrinsic-motivation.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/09/10/hierarchical-drl-intrinsic-motivation.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/09/04/VIME.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/08/16/Deep-exploration.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/08/02/A3C.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/03/23/nfq.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/03/04/AlphaGo.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/01/28/dueling-networks.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/01/26/prioritizing-experience-replay.html', 'https://pemami4911.github.io/paper-summaries/deep-rl/2016/01/22/incentivizing-exploraton-in-rl.html', 'https://pemami4911.github.io/paper-summaries/computer-vision/2018/12/26/LfD-in-the-wild.html', 'https://pemami4911.github.io/paper-summaries/computer-vision/2018/06/03/tracking-occluded-objects-by-reasoning-about-containment.html', 'https://pemami4911.github.io/paper-summaries/computer-vision/2017/05/14/DESIRE.html', 'https://pemami4911.github.io/paper-summaries/computer-vision/2017/05/04/semantic-image-seg-with-deep-g-crfs.html', 'https://pemami4911.github.io/paper-summaries/computer-vision/2017/03/28/pixel-recursive-super-res.html', 'https://pemami4911.github.io/paper-summaries/computer-vision/2016/07/30/ResNets.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2018/06/22/rudder.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2018/03/01/horde.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2017/08/29/deep-symbolic-rl.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2016/12/30/linear-least-squares-td.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2016/12/13/memory-transformations.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2016/09/16/optimal-control-of-pomdp.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2016/08/29/intrinsically-motivated-rl.html', 'https://pemami4911.github.io/paper-summaries/reinforcement-learning-theory/2016/08/11/Coop-Inverse-RL.html', 'https://pemami4911.github.io/paper-summaries/generative-adversarial-networks/2018/03/26/progressive-growing-gans.html', 'https://pemami4911.github.io/paper-summaries/generative-adversarial-networks/2017/02/12/gans-irl-ebm.html', 'https://pemami4911.github.io/paper-summaries/generative-adversarial-networks/2017/02/01/infoGAN.html', 'https://pemami4911.github.io/paper-summaries/natural-language-processing/2018/06/22/z-forcing.html', 'https://pemami4911.github.io/paper-summaries/natural-language-processing/2017/04/05/distributed-representations-of-words-and-phrases.html', 'https://pemami4911.github.io/paper-summaries/natural-language-processing/2017/01/26/neural-probabilistic-language.html', 'https://pemami4911.github.io/paper-summaries/deep-learning-theory/2020/03/22/what-can-neural-nets-reason-about.html', 'https://pemami4911.github.io/paper-summaries/deep-learning-theory/2018/04/07/convexified-cnns.html', 'https://pemami4911.github.io/paper-summaries/deep-learning-theory/2017/11/19/geometric-deep-learning.html', 'https://pemami4911.github.io/paper-summaries/deep-learning-theory/2017/08/07/deep-hessian-free.html', 'https://pemami4911.github.io/paper-summaries/deep-learning-theory/2017/03/01/batch-renorm.html', 'https://pemami4911.github.io/paper-summaries/agi/2017/05/14/interaction-networks-for-learning-about-objects-relations-physics.html', 'https://pemami4911.github.io/paper-summaries/agi/2016/05/13/learning-to-think.html', 'https://pemami4911.github.io/paper-summaries/agi/2016/01/18/review-btom.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2017/09/14/LLE.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2017/08/31/ISOMAP.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2017/06/21/mcmc-rev.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2017/04/20/topology-data.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2016/08/23/ML-for-genomics.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2016/01/29/multipolicy-decision-making.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2016/01/29/intention-aware.html', 'https://pemami4911.github.io/paper-summaries/general-ml/2016/01/21/how-to-write-a-great-research-paper.html']
data={}
i=0
redditUrl="reddit.com/"
print("Number of links",len(links))
for url in links:
    if i % 5 ==0:
        print(i)
    currBlog={}
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.decompose()
    strips = list(soup.stripped_strings)
    paperTitle=strips[0]
    transcript="\n".join(strips)
    currBlog['sourceUrl']=url
    currBlog['trancript']=transcript
    currBlog['sourceType']='blog'
    linkToPaper=""
    prev=""
    for link in soup.findAll('a'):
        # if i ==10:
            # print("Hello",link.get('href'),prev,"\n\n\n")
            
        cont=link.contents[0]
        if 'et al' in cont or redditUrl in prev:
            linkToPaper=link.get('href')
        prev=link.get('href')
    currBlog['linkToPaper']=linkToPaper
    if linkToPaper:
        data[str(i)]=currBlog
        i+=1
    else:
        print("Url is ",url)

jsonObj=json.dumps(data,indent=4)
with open('patrikEmami.json','w') as f:
    f.write(jsonObj)