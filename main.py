import pyaudio
import speech_recognition as sr
from playsound import playsound
from notifypy import Notify
from speech_recognition.exceptions import RequestError
import pyttsx3
from time import sleep
import pywhatkit as pywkt

# python tts
def ttspeech(speech_text):
  ttsengine = pyttsx3.init()
  ttsengine.setProperty('rate', 200)
  voice = ttsengine.getProperty('voices')
  ttsengine.setProperty('voice', voice[0].id)
  ttsengine.say(speech_text)
  ttsengine.runAndWait()

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
        if "max" in hotword:
          wakeup_assistant()
        else:
          wakeup_hotword()
    except sr.UnknownValueError:
      wakeup_hotword()
    except RequestError:
      ttspeech("You are not connected to the internet, Please try again later")
      print("Connection Error! Please check your connection")

def wakeup_assistant():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        notification = Notify()
        notification.application_name = "MAX"
        notification.title = "I'm here"
        notification.message = "How can I help you?\n\nPlease wait for speak notification"
        notification.icon = "./icon.png"
        notification.audio = "./rec_start.wav"
        notification.send()
        ttspeech("I'm here. How can I help you?")
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        # playsound('./rec_start.wav')
        sleep(3)
        print("Speak...")
        notification = Notify()
        notification.application_name = "MAX"
        notification.title = "Speak"
        notification.message = "Speak into the mic..."
        notification.icon = "./icon.png"
        notification.audio = "./rec_start.wav"
        notification.send()
        audio = recognizer.listen(mic)
        recognized_speech = recognizer.recognize_google(audio, language='en-US')
        recognized_text = recognized_speech.lower()
        print(recognized_text)
        hotword_detect(recognized_text)
    except sr.UnknownValueError:
      wakeup_hotword()

def voice_input():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        notification = Notify()
        notification.application_name = "MAX"
        notification.title = "Speak"
        notification.message = "Speak into the mic..."
        notification.icon = "./icon.png"
        notification.audio = "./rec_start.wav"
        notification.send()
        audio = recognizer.listen(mic)
        recognized_speech = recognizer.recognize_google(audio, language='en-US')
        search_item = recognized_speech.lower()
        from functions import search_google
        search_google(search_item)
        wakeup_hotword()
    except sr.UnknownValueError:
      ttspeech("Sorry I dont here that")
      wakeup_hotword()


def hotword_detect(hotword):
  try:
    if "google" in hotword:
      search_item = hotword.replace("search", "").replace("on", "").replace("google", "")
      from functions import search_google
      search_google(search_item)
      wakeup_hotword()
    if "search on google" in hotword:
      ttspeech("What do you want to search?")
      voice_input()
    elif "open youtube" in hotword:
      command = hotword.replace("open youtube", "opening youtube")
      from functions import open_youtube
      open_youtube(command)
      wakeup_hotword()
    elif "open whatsapp" in hotword:
      command = hotword.replace("open whatsapp", "opening whatsapp")
      from functions import open_whatsapp
      open_whatsapp(command)
      wakeup_hotword()
    elif "open instagram" in hotword:
      command = hotword.replace("open instagram", "opening instagram")
      from functions import open_instagram
      open_instagram(command)
      wakeup_hotword()
    else:
      item_not_found = hotword
      with open("check_command.txt", "a") as file:
        file.write(item_not_found +"\n")
      ttspeech("Here is what I found on the web.")
      pywkt.search(item_not_found)
      wakeup_hotword()
  except:
    wakeup_hotword()

while True:
  wakeup_hotword()