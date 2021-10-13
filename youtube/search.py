import json
import urllib.parse
import urllib.request
# from urllib.request import urlretrieve
# from urllib.parse import urlencode


def get_key(path):
    with open(path,'r') as f:
        key = json.load(f)
    return key['APIkey']

def search(path, query):
    key = get_key(path)
    print(key)
    params = {
        'part' : 'snippet',
        'type' : 'playlist',
        'q': query,
        'key': key
    }
    paramstring = urllib.parse.urlencode(params)
    print(paramstring)
    request = urllib.request.Request("https://youtube.googleapis.com/youtube/v3/search?" + paramstring)
    
    response = urllib.request.urlopen(request)
    print(json.loads(response.read()))