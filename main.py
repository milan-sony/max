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
        recognizer.dynamic_energy_threshold = True
        playsound('./rec_start.wav')
        print("Listening...")
        audio = recognizer.listen(mic)
        recog_audio= recognizer.recognize_google(audio)
        hotword = recog_audio.lower()
        if "max" or "hey max" or "heymax" or "hay max" or "haymax" or "hello max" or "hellomax" or "wakup max" or "wakeupmax" in hotword:
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
        print("I am here, How can I help you?")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        recognizer.dynamic_energy_threshold = True
        playsound('./rec_start.wav')
        print("Speak...")
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


