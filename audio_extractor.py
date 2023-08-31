
import azure.cognitiveservices.speech as speechsdk
import time
import pickle

from moviepy.editor import VideoFileClip

from dotenv import dotenv_values

def extract_audio(filename):
    video = VideoFileClip(filename)
    audio = video.audio
    output = filename + ".audio_only.wav"
    audio.write_audiofile(output)
    return output

# https://northeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken
# 

config = dotenv_values(".env")
speech_api_key = config.get("AZURE_SPEECH_API_KEY", None)
speech_region = config.get("AZURE_SPEECH_REGION", None)

# print( "speech_api_key: " + speech_api_key)
# print( "speech_region: " + speech_region)

filename = "C:/Meetings/03DAI/FY24 Data & AI Landing Live Show - July 2023.mp4"

audio_file = extract_audio(filename)
