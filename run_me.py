# 
# Main entry point 
# 

from audio_extractor import extract_audio
from subtitle_creator import subtitle_creator

# from process_docx import process_docx
# from process_vtt import *

filename = "C:/Recordings/02/Learning Day Vector Search with Azure Cognitive Search-20230317_190209-Meeting Recording.mp4"
print( "Hello world")
# extract audio file
audio_output = extract_audio(filename)

# create subtitles
sc = subtitle_creator(audio_output)
output = sc.transcribe_text()
print("TEXT transcribed: " + output)


