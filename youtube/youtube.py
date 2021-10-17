

"""
Given a Youtube Playlist URL, transcribes all videos to a JSON.
If captions available then uses that.
If not available then downloads audio and uses IBM Watson API for caption.
Also has an option to override such that Watson API is used always and auto-caption is discarded even if present.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs, urlparse
import googleapiclient.discovery
import watson_transcript
import argparse
import creds
import json


def get_playlist_items(playlist_url):
    query = parse_qs(urlparse(playlist_url).query, keep_blank_values=True)
    playlist_id = query["list"][0]

    print(f'get all playlist items links from {playlist_id}')
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = creds.youtube_api_key)

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


def dump_playlist_descriptions_and_transcripts_to_json(playlist_url, json_filename, watson_override):
    playlist_items = get_playlist_items(playlist_url)
    results = []
    ctr = 0
    for playlist_item in playlist_items:
        description = playlist_item['snippet']['description']
        video_id = playlist_item['snippet']['resourceId']['videoId']
        video_title = playlist_item['snippet']['title']
        position_in_playlist = playlist_item['snippet']['position']

        if description == "This video is private.":
            print(video_id, "is private video.")
            continue

        if watson_override:
            try:
                transcript = watson_transcript.transcript(video_id, video_title)
                transcription_mode = "IBM Watson"
            except:
                transcript = "NA"
                transcription_mode = "NA"
        else:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                transcript = ' '.join([t['text'] for t in transcript]).replace('\n',' ')
                transcription_mode = "YouTube Transcript API"
            except:
                try:
                    transcript = watson_transcript.transcript(video_id, video_title)
                    transcription_mode = "IBM Watson"
                except:
                    transcript = "NA"
                    transcription_mode = "NA"

        result ={
                "video_id": video_id,
                "video_title": video_title,
                "position_in_playlist": position_in_playlist,
                "description": description,
                "transcript": transcript,
                "transcription_mode": transcription_mode
                }
        results.append(result)
        ctr += 1
        print(video_id, "Done!", "Counter:", ctr)
    fp = open(json_filename, 'w')
    json.dump(results, fp, sort_keys=False, indent=4)
    fp.close()



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--playlist_url", type=str, required=True)
    parser.add_argument("--json_filename", type=str, required=True)
    parser.add_argument('--override_with_watson', type=bool, default=False)
    args = parser.parse_args()
    dump_playlist_descriptions_and_transcripts_to_json(args.playlist_url, \
            args.json_filename, args.override_with_watson)


if __name__ =="__main__":
    main()

