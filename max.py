import pyaudio
import speech_recognition as sr
from notifypy import Notify
from speech_recognition.exceptions import RequestError
import pyttsx3
from time import sleep
from datetime import date
import time

def wakeup_hotword():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        print("Listening...")
        audio = recognizer.listen(mic)
        recognized_speech = recognizer.recognize_google(audio, language='en-US')
        hotword = recognized_speech.lower()
        if ("max" in hotword) or ("hey max" in hotword) or ("hay max" in hotword) or ("heymax" in hotword) or ("haymax" in hotword):
          wakeup_assistant()
        else:
          wakeup_hotword()
    except sr.UnknownValueError:
      wakeup_hotword()
    except RequestError:
      ttspeech("Connection Error, Make sure you are connected to the Internet!", 150)
      print("Connection Error! Please check your connection")
