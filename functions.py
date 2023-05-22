import pyttsx3
from playsound import playsound

# python tts
def ttspeech(speech_text):
  ttsengine = pyttsx3.init()
  rate = ttsengine.getProperty('rate')
  ttsengine.setProperty('rate', rate+15)
  ttsengine.say(speech_text)
  ttsengine.runAndWait()

# open youtube
def open_youtube(command):
  ttspeech(command)
  print("hello from youtube")
  playsound('./rec_stop.wav')
