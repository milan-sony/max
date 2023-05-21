import pyaudio
import speech_recognition as sr
from time import sleep
from notifypy import Notify

def listen_for_hotword():
  recognizer = sr.Recognizer()
  with sr.Microphone(device_index=0) as source:
    print("Listening...")
    audio = recognizer.listen(source)
  try:
    # Google Speech Recognition engine
    hotword = recognizer.recognize_google(audio)
    if hotword == "hello":
      wake_up_assistant()
  except sr.UnknownValueError:
    sleep(10)
    listen_for_hotword()

def wake_up_assistant():
  recognizer = sr.Recognizer()
  with sr.Microphone(device_index=0) as source:
    notification = Notify()
    notification.application_name = ""
    notification.title = f"CODEY"
    notification.message = f""
    notification.icon = "./icon.png"
    notification.audio = "./notificationsound.wav"
    notification.send()
    print("I am here, How can I help you?")
    audio = recognizer.listen(source)
    try:
      commamd = recognizer.recognize_google(audio)
      print("You have said: "+ commamd)
    except sr.UnknownValueError:
      pass




while True:
  listen_for_hotword()
