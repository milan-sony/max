import pyttsx3
from playsound import playsound
from time import sleep
import webbrowser
import pywhatkit as pywkt
from AppOpener import open, close

def ttspeech(speech_text):
  ttsengine = pyttsx3.init()
  ttsengine.setProperty('rate', 160)
  voice = ttsengine.getProperty('voices')
  ttsengine.setProperty('voice', voice[0].id)
  ttsengine.say(speech_text)
  ttsengine.runAndWait()

def search_google(search_item):
  ttspeech("Searching" +search_item+ "on google")
  pywkt.search(search_item)

def open_urls(url):
  webbrowser.open_new_tab(url)
  sleep(1)
  playsound('./rec_stop.wav')

def open_applications(command):
  ttspeech("Opening" +command)
  open(command)
  playsound('./rec_stop.wav')

def open_in_browser(command):
  if ("instagram" in command):
    ttspeech("Opening" +command)
    url = "https://www.instagram.com/"
    open_urls(url)
  elif ("youtube" in command):
    ttspeech("Opening" +command)
    url = "https://www.youtube.com/"
    open_urls(url)
  elif ("whatsapp" in command) or ("whatsappweb" in command) or ("whatsapp web" in command):
    ttspeech("Opening" +command)
    url = "https://web.whatsapp.com/"
    open_urls(url)
  else:
    pass