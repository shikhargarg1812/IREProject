

"""
Given data from scraped conference website, transcripts the YouTube videos.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs, urlparse
import watson_transcript
import argparse
import creds
import json
import pandas as pd


def dump_data(conference_csv, json_filename, watson_override):
    df = pd.read_csv("nips_2019.csv")
    results = []
    ctr = 0
    for index in range(len(df)):
        paper_link, paper_pdf_link, paper_title, paper_author, video_link, abstract = df.iloc[index].tolist()
        if '&' in video_link:
            video_link = video_link.split('&')[0]
        if '?t=' in video_link:
            video_link = video_link.split('?t=')[0]
        if "you" in video_link:
            if "watch?v=" in video_link:
                video_id = video_link.split('=')[1]
            elif "https://youtu.be/" in video_link:
                video_id = video_link.split('/')[-1]
            else:
                print(video_link, "None of others")
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
        else:
            # Non Youtube
            transcript = "NA"
            transcription_mode = "NA"
        result ={
                "paper_link": paper_link,
                "paper_pdf_link": paper_pdf_link,
                "paper_title": paper_title,
                "paper_author": paper_author,
                "video_link": video_link,
                "abstract": abstract,
                "transcript": transcript,
                "transcription_mode": transcription_mode
                }
        f = open("res/{}.json".format(index), 'w')
        json.dump(result, f, sort_keys=False, indent=4)
        f.close()
        results.append(result)
        ctr += 1
    fp = open(json_filename, 'w')
    json.dump(results, fp, sort_keys=False, indent=4)
    fp.close()



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference_csv", type=str, default="nips_2019.csv")
    parser.add_argument("--json_filename", type=str, default="nips_2019.json")
    parser.add_argument('--override_with_watson', type=bool, default=False)
    args = parser.parse_args()
    dump_data(args.conference_csv, \
            args.json_filename, args.override_with_watson)


if __name__ =="__main__":
    main()

