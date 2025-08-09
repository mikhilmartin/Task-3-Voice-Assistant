import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

# Setup
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def hear():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        talk("Hmm, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        talk("Oops! There seems to be a network issue.")
        return ""

def run_jarvis(command):
    command = command.lower()

    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"It's {now}")

    elif "date" in command:
        today = datetime.date.today().strftime("%A, %B %d")
        talk(f"Today is {today}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            talk(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            talk("What would you like me to search for?")

    elif "youtube" in command:
        talk("Sure, opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "quit" in command or "stop" in command:
        talk("Goodbye! Have a great day.")
        sys.exit()

    else:
        talk("I'm still learning. Can you try saying it differently?")

# Main loop
if __name__ == "__main__":
    talk("Hello! I'm Jarvis, your assistant. What can I do for you?")
    while True:
        command = hear()
        if command:
            run_jarvis(command)
