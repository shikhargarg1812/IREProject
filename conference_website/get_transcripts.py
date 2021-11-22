

"""
Given data from scraped conference website, transcripts the YouTube videos.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs, urlparse
import googleapiclient.discovery
import watson_transcript
import argparse
import creds
import json
import pandas as pd


def dump_data(conference_csv, json_filename, watson_override):
    df = pd.read_csv("nips_2019.csv")
    # is_youtube = ['you' in item for item in df['video_links']]
    # df = df[is_youtube]

    results = []
    ctr = 0
    for index in len(df):
        paper_link, paper_pdf_link, paper_title, paper_author, video_link = df.iloc[index].tolist()
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_link)
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
                "transcript": transcript,
                "transcription_mode": transcription_mode
                }
        results.append(result)
        ctr += 1
    fp = open(json_filename, 'w')
    json.dump(results, fp, sort_keys=False, indent=4)
    fp.close()



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference_csv", type=str, required=True)
    parser.add_argument("--json_filename", type=str, required=True)
    parser.add_argument('--override_with_watson', type=bool, default=False)
    args = parser.parse_args()
    dump_data(args.conference_csv, \
            args.json_filename, args.override_with_watson)


if __name__ =="__main__":
    main()

