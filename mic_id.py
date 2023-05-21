# print all the microphones connected to your machine
from pvrecorder import PvRecorder
def mic_id():
  for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"NAME: {device}, ID: {index}")

mic_id()