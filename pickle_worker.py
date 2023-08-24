import pickle
import pprint



filename = "C:/Meetings/03DAI/FY24 Data & AI Landing Live Show - July 2023.mp4.audio_only.wav.transcribed_video.pickle"

obj = pickle.load(open(filename, "rb"))


print(obj)

# with open("out.txt", "a") as f:
#    pprint.pprint(obj, stream=f)
#    f.close()
