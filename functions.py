import pyttsx3
from playsound import playsound
from time import sleep
import webbrowser
import pywhatkit as pywkt
from AppOpener import open, close
import os
import main

# text to speech
def ttspeech(speech_text):
  ttsengine = pyttsx3.init()
  ttsengine.setProperty('rate', 160)
  voice = ttsengine.getProperty('voices')
  ttsengine.setProperty('voice', voice[0].id)
  ttsengine.say(speech_text)
  ttsengine.runAndWait()

# default search
def default_search(search_item):
  pywkt.search(search_item)
  playsound("./rec_stop.wav")
  # main.wakeup_hotword()

# search on google
def search_on_google(search_item):
  ttspeech("Searching" +search_item+ "on google")
  pywkt.search(search_item)
  # main.wakeup_hotword()

system_applications = [
  "notepad",
  "chrome",
  "settings",
  "alaram",
]
web_applications = [
  "youtube",
  "instagram",
  "facebook",
  "whatsapp",
]

# open an application
def open_appications(command):
  print(command)
  if command in system_applications:
    os.system(command)
  elif command in web_applications:
    url = f"https://www.{command}.com/"
    webbrowser.open_new_tab(url)
  else:
    ttspeech("Sorry app not found")
    # main.wakeup_hotword()

# close an applicaton
def close_applications(command):
  print(command)
  if command in system_applications:
    os.system(f'wmic process where name="{command}" delete')
  elif command in web_applications:
    url = f"https://www.{command}.com/"
    webbrowser.open_new_tab(url)
  else:
    ttspeech("Sorry app not found")
    # main.wakeup_hotword()