# notify-py==0.3.41

from notifypy import Notify

# Desktop notification
notification = Notify()
notification.application_name = "Weather Update"
notification.title = f"Weather at {city_name}"
notification.message = f"🌡️ Temperature: {temp_roundfig}°C      Feels like: {feels_like_roundfig}°C \n{weather_desc_capitalize}"
notification.icon = "./icon.png"
notification.audio = "./notificationsound.wav"
notification.send()