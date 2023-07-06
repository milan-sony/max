import eel

# initializing the application
eel.init("web")

# exposing the function to javascript
@eel.expose
def user_input(msg):
    return msg

def asst_input(msg):
    return msg

def start():
    eel.start("index.html", size=(800,500))