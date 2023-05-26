import pyaudio
import speech_recognition as sr
from notifypy import Notify
from speech_recognition.exceptions import RequestError
import pyttsx3
from time import sleep
from datetime import date
import time

# tts
def ttspeech(speech_text, rate):
  ttsengine = pyttsx3.init()
  speech_rate  = rate
  ttsengine.setProperty(f'rate', int(speech_rate))
  voice = ttsengine.getProperty('voices')
  ttsengine.setProperty('voice', voice[0].id)
  ttsengine.say(speech_text)
  ttsengine.runAndWait()

# desktop notification
def desktop_notification(title, message):
  notification_title = str(title)
  notification_message = str(message)
  notification = Notify()
  notification.application_name = "MAX"
  notification.title = notification_title
  notification.message = notification_message
  notification.icon = "./icon.png"
  notification.audio = "./rec_start.wav"
  notification.send()

# listen for hotword
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

# wake up assistant after the hotword is detected
def wakeup_assistant():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        desktop_notification(
          "I'm here",
          "How can I help you?\n\nPlease wait for speak notification"
        )
        ttspeech("I'm here. How can I help you?", 200)
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        sleep(3)
        print("Speak...")
        desktop_notification(
          "Speak",
          "Speak into the mic..."
        )
        audio = recognizer.listen(mic)
        recognized_speech = recognizer.recognize_google(audio, language='en-US')
        recognized_text = recognized_speech.lower()
        print(recognized_text)
        hotword_detect(recognized_text)
    except sr.UnknownValueError:
      wakeup_hotword()

# voice search input
def voice_input():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        desktop_notification(
          "Speak",
          "Speak into the mic..."
        )
        audio = recognizer.listen(mic)
        recognized_speech = recognizer.recognize_google(audio, language='en-US')
        search_item = recognized_speech.lower()
        from functions import search_on_google
        search_on_google(search_item)
        wakeup_hotword()
    except sr.UnknownValueError:
      ttspeech("Sorry I dont here that", 200)
      wakeup_hotword()

# hotword detection
def hotword_detect(hotword):
  try:
    if ("search on google" in hotword):
      ttspeech("What do you want to search?", 200)
      voice_input()
    elif("open" in hotword):
      command = hotword.replace("open","").replace(" ","")
      from functions import open_appications
      open_appications(command)
      wakeup_hotword()
    elif("close" in hotword):
      command = hotword.replace("close", "").replace(" ","")
    else:
      item_not_found = hotword
      current_date = date.today()
      dt = current_date.strftime("%d %B %Y")
      current_time = time.localtime()
      formatted_time = time.strftime("%I:%M:%S %p", current_time)
      with open("check_command.txt", "a") as file:
        file.write("Date: "+dt+"\n"+"Time: "+formatted_time+"\n"+"Command: "+item_not_found+"\n"+"-----------------------------------"+"\n")
        ttspeech("Here is what I found on the web.", 200)
      from functions import default_search
      default_search(item_not_found)
      wakeup_hotword()
  except:
    wakeup_hotword()

while True:
  wakeup_hotword()