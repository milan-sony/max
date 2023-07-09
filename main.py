import pyaudio
import speech_recognition as sr
from notifypy import Notify
from speech_recognition.exceptions import RequestError
import pyttsx3
from time import sleep
from datetime import date
import time
from tkinter import *
from playsound import playsound
import threading
import functions


def show_popup(msg, delay_value):
    # popup = tk.Toplevel()
    popup = Tk()
    popup.attributes("-topmost", 1)
    popup.title("M A X")
    popup.iconbitmap("./icon.ico")
    popup.geometry("300x100")
    playsound('./rec_start.wav')
    popup.config(bg="#6886C5")
    popup.resizable(False, False)

    label = Label(popup,
                  text=str(msg),
                  font="Impact 15",
                  fg="#F9F9F9",
                  bg="#6886C5",
                  )
    label.pack()

    # Close the popup after 5 seconds
    popup.after(delay_value, popup.destroy)

    popup.mainloop()

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
        # recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        # recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 0.8
        print("Listening...")
        # recognized_speech = recognizer.recognize_google(audio, language='en-US')
        audio = recognizer.listen(mic, phrase_time_limit=5)
        recognized_speech = recognizer.recognize_google(audio)
        hotword = recognized_speech.lower()
        print(hotword)
        if ("max" in hotword) or ("hey max" in hotword) or ("hay max" in hotword) or ("heymax" in hotword) or ("haymax" in hotword) or ("hemex" in hotword) or ("he mex" in hotword):
          wakeup_assistant()
        else:
          print("hotword not max")
          # wakeup_hotword()
    except sr.UnknownValueError:
      print("Sorry I don't understand that")
      # wakeup_hotword()
    except RequestError:
      ttspeech("Connection Error, Make sure you are connected to the Internet!", 150)
      print("Connection Error! Please check your connection")
      show_popup("Connection Error!\nPlease check your connection")

# wake up assistant after the hotword is detected
def wakeup_assistant():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        # desktop_notification(
        #   "I'm here",
        #   "How can I help you?\n\nPlease wait for speak notification"
        # )
        recognizer.pause_threshold = 0.8
        # show_popup("I'm here.\nHow can I help you?")
        show_popup("MAX", 1000)
        ttspeech("I'm here. How can I help you?", 200)
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        recognizer.dynamic_energy_threshold = True
        show_popup("Speak...", 2000)
        print("Speak...")
        # desktop_notification(
        #   "Speak",
        #   "Speak into the mic..."
        # )
        audio = recognizer.listen(mic)
        # recognized_speech = recognizer.recognize_google(audio, language='en-US')
        recognized_speech = recognizer.recognize_google(audio)
        recognized_text = recognized_speech.lower()
        print(recognized_text)
        hotword_detect(recognized_text)
    except sr.UnknownValueError:
      print("Sorry")
      show_popup("Sorry\nI don't understand that", 2000)
      ttspeech("Sorry I don't understand that", 200)
      wakeup_hotword()

# voice search input
def voice_input():
  recognizer = sr.Recognizer()
  done = False
  while not done:
    try:
      with sr.Microphone() as mic:
        # recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        # recognizer.dynamic_energy_threshold = True
        # desktop_notification(
        #   "Speak",
        #   "Speak into the mic..."
        # )
        recognizer.pause_threshold = 0.8
        show_popup("Speak", 2000)
        audio = recognizer.listen(mic, phrase_time_limit=5)
        recognized_speech = recognizer.recognize_google(audio, language='en-US')
        search_item = recognized_speech.lower()
        from functions import search_on_google
        search_on_google(search_item)
        # wakeup_hotword()
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
      functions.open_appications(command)
      # wakeup_hotword()
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
      functions.default_search(item_not_found)
      # wakeup_hotword()
  except:
    print("Item not found")
    wakeup_hotword()

t1 = threading.Thread(target=wakeup_hotword)
t1.start() 
t1.join()