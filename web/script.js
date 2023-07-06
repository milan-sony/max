let assistMsg = document.getElementById("assistant-message")
let userMsg = document.getElementById("user-message")

eel.expose(user_input)
eel.expose(asst_input)

function user_input(msg){
    userMsg.innerText=msg
}

function asst_input(msg){
    assistMsg.innerText = msg
}