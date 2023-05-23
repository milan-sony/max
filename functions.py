import pyttsx3
from playsound import playsound
from time import sleep
import webbrowser
import pywhatkit as pywkt

# python tts
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

def open_url(url):
  webbrowser.open_new_tab(url)
  sleep(1)
  playsound('./rec_stop.wav')

def open_youtube(command):
  ttspeech(command)
  url = "https://www.youtube.com/"
  open_url(url)

def open_whatsapp(command):
  ttspeech(command)
  url = "https://web.whatsapp.com/"
  open_url(url)

def open_instagram(command):
  ttspeech(command)
  url = "https://www.instagram.com/"
  open_url(url)
