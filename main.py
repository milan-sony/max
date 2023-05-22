import pyaudio
import speech_recognition as sr
from time import sleep
from playsound import playsound
from notifypy import Notify
from speech_recognition.exceptions import RequestError
def listen_for_hotword():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
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
    except RequestError:
      print("Connection Error! Please check your connection")

def wakeup_assistant():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        # print("I am here, How can I help you?")
        notification = Notify()
        notification.application_name = "MAX"
        notification.title = "I'm here"
        notification.message = "How can I help you?"
        notification.icon = "./icon.png"
        notification.audio = "./rec_start.wav"
        notification.send()
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        # playsound('./rec_start.wav')
        print("Speak...")
        audio = recognizer.listen(mic)
        recog_audio= recognizer.recognize_google(audio)
        hotword = recog_audio.lower()
        print("You have said: "+hotword)
        playsound('./rec_stop.wav')
        listen_for_hotword()
    except sr.UnknownValueError:
      listen_for_hotword()
    raise 

while True:
  listen_for_hotword()


