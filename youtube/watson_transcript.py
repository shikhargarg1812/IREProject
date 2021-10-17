

import dl_audio
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import subprocess
import creds


authenticator = IAMAuthenticator(creds.watson_api_key)
service = SpeechToTextV1(authenticator = authenticator)
service.set_service_url(creds.watson_api_url)


def transcript(video_id, title):
    os.makedirs("audio_files", present_ok=True)
    webm_file = os.path.join("audio_files", title+'.webm')
    flac_file = os.path.join("audio_files", title+'.flac')

    dl_audio.download_audio(video_id, webm_file)
    command = ["ffmpeg", "-i", webm_file, "-c:a", "flac", flac_file]
    print(' '.join(command))
    subprocess.run(command)

    audio_file = open(flac_file,'rb')
    res = service.recognize(audio=audio_file,content_type='audio/flac').get_result()
    text = " ".join([r['alternatives'][0]['transcript'] for r in res['results']])
    return text

