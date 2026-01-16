# voice_agriculture_control.py
import requests
import pyttsx3
import speech_recognition as sr
import time

# ---------------- CONFIGURATION ----------------
ESP32_IP = "192.168.75.151"  # Replace with your ESP32 IP
COMMAND_TIMEOUT = 2           # HTTP request timeout in seconds

# ---------------- TEXT-TO-SPEECH ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def say(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- ESP32 CONNECTIVITY ----------------
def send_command(device, action):
    """Send HTTP request to ESP32 to control devices"""
    url = f"http://{ESP32_IP}/control"
    payload = {device: action}
    try:
        response = requests.get(url, params=payload, timeout=COMMAND_TIMEOUT)
        if response.status_code == 200:
            say(f"{device.upper()} set to {action.upper()}")
        else:
            say(f"Failed to set {device}. Server returned {response.status_code}")
    except Exception as e:
        say(f"Could not send command to ESP32: {e}")

# ---------------- SPEECH RECOGNITION ----------------
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command... Speak now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; check network:", e)
        return ""

# ---------------- MAIN PROGRAM ----------------
say("Smart Agriculture Voice Control System Activated")

while True:
    command = listen_command()

    if not command:
        continue

    # ----- PUMP COMMANDS -----
    if "pump on" in command or "turn on irrigation" in command:
        send_command("pump", "on")
    elif "pump off" in command or "stop irrigation" in command:
        send_command("pump", "off")
    elif "pump auto" in command or "automatic irrigation" in command:
        send_command("pump", "auto")

    # ----- LED COMMANDS -----
    elif "led on" in command or "turn on light" in command:
        send_command("led", "on")
    elif "led off" in command or "turn off light" in command:
        send_command("led", "off")
    elif "led auto" in command or "automatic light" in command:
        send_command("led", "auto")

    # ----- MOTOR COMMANDS -----
    elif "motor on" in command or "turn on fan" in command:
        send_command("motor", "on")
    elif "motor off" in command or "turn off fan" in command:
        send_command("motor", "off")
    elif "motor auto" in command or "automatic fan" in command:
        send_command("motor", "auto")

    # ----- EXIT -----
    elif "exit" in command or "stop assistant" in command or "quit" in command:
        say("Voice control system stopped")
        break

    time.sleep(1)
