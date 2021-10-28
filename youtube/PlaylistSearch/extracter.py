import sys
import search
import json

path = sys.argv[1]
query = sys.argv[2]

next_page = 'first'

metafile = open('data.txt','w')

while next_page != 'last':
    search_res, next_page = search.get_searched_playlists(path, query, next_page)

    for i in search_res.keys():
        print(i)
        metadata = search.get_playlist_items(path, i)
        print(json.dumps(metadata),file=metafile)