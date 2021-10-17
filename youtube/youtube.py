
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
from youtube_transcript_api import YouTubeTranscriptApi

KEY = "AIzaSyArK2BYnwnm8b72atyLRP-liNJkFphIZpk"


def get_playlist_items(playlist_url):
    query = parse_qs(urlparse(playlist_url).query, keep_blank_values=True)
    playlist_id = query["list"][0]

    print(f'get all playlist items links from {playlist_id}')
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = KEY)

    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)
    return playlist_items


def dump_playlist_descriptions_and_transcripts_to_json(playlist_url, json_filename):
    playlist_items = get_playlist_items()
    results = []
    for playlist_item in playlist_items:
        description = playlist_item['snippet']['description']
        video_id = playlist_item['snippet']['resourceId']['videoId']
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([t['text'] for t in transcript]).replace('\n',' ')

        results.append(
            {
                "video_id": video_id,
                "description": description,
                "transcript": transcript
            }
        )
    f = open(json_filename, 'w')
    json.dump(results)
    f.close()


def main():
    dump_playlist_descriptions_and_transcripts_to_json( \
        playlist_url =  "https://www.youtube.com/playlist?list=PLujxSBD-JXgnqDD1n-V30pKtp6Q886x7e" \
        json_filename = "TwoMinutePapers.json"
    )

if __name___ =="__main__":
    main()