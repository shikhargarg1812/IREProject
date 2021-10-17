

import dl_audio
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import subprocess

API_KEY = "eEowFPzQDZhHAf2dQlKWADcHmPbaAjjQb-X_lCt-flx_"
API_URL = "https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/c9f8637e-ed45-4217-820d-f7b1df10c1b5"

authenticator = IAMAuthenticator(API_KEY)
service = SpeechToTextV1(authenticator = authenticator)
service.set_service_url(API_URL)


def transcript(video_id, title):
    os.makedirs("audio_files", present_ok=True)
    webm_file = os.path.join("audio_files", title+'.webm')
    flac_file = os.path.join("audio_files", title+'.flac')

    dl_audio.download_audio(video_id, webm_file)
    command = "ffmpeg -i {} -c:a flac {}".format(webm_file, flac_file)
    print(command)
    subprocess.run(command.split())

    audio_file = open(flac_file,'rb')
    res = service.recognize(audio=audio_file,content_type='audio/flac').get_result()
    text = " ".join([r['alternatives'][0]['transcript'] for r in res['results']])
    return text

