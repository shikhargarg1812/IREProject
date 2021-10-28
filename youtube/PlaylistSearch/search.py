import json
import urllib.parse
import urllib.request
import process
# from urllib.request import urlretrieve
# from urllib.parse import urlencode


def __get_key(path):
    with open(path,'r') as f:
        key = json.load(f)
    return key['API_cred']

def get_searched_playlists(path, query, pageToken):
    key = __get_key(path)
    
    params = {
        'part' : 'snippet',
        'type' : 'playlist',
        'q': query,
        'key': key,
        'maxResults':50
    }

    if pageToken != 'first':
        params['pageToken'] = pageToken

    paramstring = urllib.parse.urlencode(params)
    request = urllib.request.Request("https://youtube.googleapis.com/youtube/v3/search?" + paramstring)
    
    response = urllib.request.urlopen(request)
    
    results = json.loads(response.read())

    next_page = 'last'
    if 'nextPageToken' in results:
            next_page = results['nextPageToken']

    playlist_ids = {}
    for i in results["items"]:
        playlist_ids[i["id"]["playlistId"]] = i["snippet"]["title"]

    return playlist_ids,next_page

def get_playlist_items(path, playlistId):
    key = __get_key(path)
    
    page_no = 1
    params = {
            'part' : 'snippet',
            'key': key,
            'playlistId':playlistId
    }
    next_page = ''
    vids_metadata = []

    while page_no != 'last':
        if page_no != 1:
            params['pageToken'] = next_page

        paramstring = urllib.parse.urlencode(params)
        request = urllib.request.Request("https://www.googleapis.com/youtube/v3/playlistItems?" + paramstring)

        response = urllib.request.urlopen(request)
        results = json.loads(response.read())
        
        if 'nextPageToken' in results:
            next_page = results['nextPageToken']
            page_no += 1
        else:
            page_no = 'last'
        

        for i in results["items"]:
            vid = {}
            vid['id']          = i['id']
            vid['title']       = i['snippet']['title'].lower()
            vid['description'] = i['snippet']['description'].lower()
            vid['links'] = process.get_links(i['snippet']['description'].lower())
            vids_metadata.append(vid)
        
    return vids_metadata