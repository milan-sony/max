import pyaudio
import speech_recognition as sr
from time import sleep
from playsound import playsound

def listen_for_hotword():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        print("Listening...")
        playsound('./rec_start.wav')
        audio = recognizer.listen(mic)
        recog_audio= recognizer.recognize_google(audio)
        hotword = recog_audio.lower()
        if hotword == "hello":
          wakeup_assistant()
        else:
          listen_for_hotword()
    except sr.UnknownValueError:
      listen_for_hotword()

def wakeup_assistant():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        print("I am here, How can I help you?")
        audio = recognizer.listen(mic)
        recog_audio= recognizer.recognize_google(audio)
        hotword = recog_audio.lower()
        print("You have said: "+hotword)
        playsound('./rec_stop.wav')
        listen_for_hotword()
    except sr.UnknownValueError:
      listen_for_hotword()

while True:
  listen_for_hotword()


