# print all the microphones connected to your machine
import speech_recognition as s_r
for lists in s_r.Microphone.list_microphone_names():
  print(lists) 

# 2nd method
from pvrecorder import PvRecorder
for index, device in enumerate(PvRecorder.get_audio_devices()):
  print(f"[{index}] {device}")