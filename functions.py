import pyttsx3
from playsound import playsound
from time import sleep

# python tts
def ttspeech(speech_text):
  ttsengine = pyttsx3.init()
  ttsengine.setProperty('rate', 160)
  voice = ttsengine.getProperty('voices')
  ttsengine.setProperty('voice', voice[0].id)
  ttsengine.say(speech_text)
  ttsengine.runAndWait()

# open youtube
def open_youtube(command):
  ttspeech(command)
  print("hello from youtube")
  sleep(1)
  playsound('./rec_stop.wav')
