from pyscript import document, window
import re
def signUp():
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    msg = ""
    if not username or not password:
        msg = "ⓘ Please fill out all fields"
    elif len(password) < 10:
        msg = "ⓘ Password must be at least 10 characters"
    elif not re.search(r"[A-Za-z]", password):
        msg = "ⓘ Password must contain at least one letter"
    elif not re.search(r"\d", password):
        msg = "ⓘ Password must contain at least one number"
    if msg:
        document.getElementById("result").innerText = msg
        window.passwordOK = False
        document.getElementById("signup").innerText = 'Sign Up'
        return
    window.sessionStorage.setItem("username", username)
    document.getElementById("signup").innerText = 'Loading...'
    document.getElementById("result").innerText = f"Welcome, {username}!"
    window.passwordOK = True
    def do_redirect():
        if window.passwordOK:
            window.location.href = 'TEAMCHECKER.html'
    window.setTimeout(do_redirect, 5)


def showPlayers():
    container = document.getElementById("listContainer")
    if container:
        container.style.opacity = "1"

window.signUp = signUp
window.showPlayers = showPlayers