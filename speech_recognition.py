```python
import speech_recognition as sr

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio_file):
        # use the audio file as the audio source
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def test_speech_recognition():
    speech_recognition = SpeechRecognition()
    text = speech_recognition.recognize_speech('audio.wav')
    print(text)

if __name__ == "__main__":
    test_speech_recognition()
```
