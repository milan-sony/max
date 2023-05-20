import speech_recognition as sr

def listen_for_hotword():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for hotword...")
        audio = r.listen(source)

    try:
        hotword = r.recognize_google(audio)
        if hotword == "hotword":
            print("Hotword recognized, waking up assistant...")
            wake_up_assistant()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Error occurred: {0}".format(e))

def wake_up_assistant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant is awake. How can I help you?")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        # process command here
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Error occurred: {0}".format(e))

while True:
    listen_for_hotword()
