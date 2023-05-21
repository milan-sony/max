import pyaudio
import speech_recognition as sr

"""
https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14

"""

recognizer = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    recognized_text = recognizer.recognize_google(audio)  # Use Google Speech Recognition engine
    print("Recognized Text:", recognized_text)
except sr.UnknownValueError:
    print("Unable to recognize speech.")
except sr.RequestError:
    print("Could not retrieve results from the service.")