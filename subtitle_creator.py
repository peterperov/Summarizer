
import azure.cognitiveservices.speech as speechsdk
import time
import pickle
from dotenv import dotenv_values


class subtitle_creator():

    config = dotenv_values(".env")
    speech_api_key = config.get("AZURE_SPEECH_API_KEY", None)
    speech_region = config.get("AZURE_SPEECH_REGION", None)
    results = list()
    done = False
    filename = ""

    def __init__(self, filename):
        self = self
        self.filename = filename
        # Authenticate
        self.speech_config = speechsdk.SpeechConfig(self.speech_api_key, self.speech_region)
        # Set up the file as the audio source
        self.audio_config = speechsdk.AudioConfig(filename=filename)
      


    def stop_cb(self, evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        self.done = True
        print(f"CLOSING on {evt}")
        self.speech_recognizer.stop_continuous_recognition()
        # Let the function modify the flag defined outside this function
        # global done
        print(f"CLOSED on {evt}")


    def recognised(self, evt):
        """Callback to process a single transcription"""
        recognised_text = evt.result.text
        # Simply append the new transcription to the running list
        self.results.append(recognised_text)
        print(f"Audio transcription: '{recognised_text}'")


# another way of handling stop handler is here:
# https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/samples/python/console/speech_sample.py

    def transcribe_text(self):
        speech_recognizer = speechsdk.SpeechRecognizer(self.speech_config, self.audio_config)  

        # Flag to end transcription
        self.done = False

        # List of transcribed lines
        self.results = list()

        # Define behaviour for each recognition/transcription
        speech_recognizer.recognized.connect(self.recognised)

        # Define behaviour for end of session
        speech_recognizer.session_stopped.connect(self.stop_cb)
        # And for canceled sessions
        speech_recognizer.canceled.connect(self.stop_cb)

        # Create a synchronous continuous recognition, the transcription itself if you will
        speech_recognizer.start_continuous_recognition()
        # Set a brief pause between API calls
        while not self.done:
            time.sleep(0.5)

        # Dump the whole transcription to a pickle file
        with open(self.filename + ".transcribed_video.pickle", "wb") as f:
            pickle.dump(self.results, f)
            print("Transcription dumped")

        txt_output = self.filename + ".transcribed_video.txt"

        with open(txt_output, "w") as f:
            for line in self.results:
                f.write(line)
                f.write("\n")
            print("text dumped")
        
        return txt_output




# filename = "C:/Meetings/03DAI/FY24 Data & AI Landing Live Show - July 2023.mp4.audio_only.wav"

# filename = "C:/Meetings/00-Youtube/NVIDIA DLSS 3.5 _ New Ray Reconstruction Enhances Ray Tracing with AI (2160p_30fps_AV1-128kbit_AAC).mp4.audio_only.wav"
# sc = subtitle_creator(filename)
# output = sc.transcribe_text()
# print("TEXT transcribed: " + output)