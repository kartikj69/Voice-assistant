import os
from plyer import notification
import smtplib
import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import wikipedia
import webbrowser
import time
import logging
from config import EMAIL, PASSWORD, MUSIC_DIR, CODE_PATH

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Function to wish the user based on the time of the day"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am your assistant, your excellency. Please tell me how may I help you?")

def take_command():
    """Function to take voice command from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logging.info("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        logging.info("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        logging.info(f"User said: {query}\n")
    except Exception as e:
        logging.error(e)
        logging.info("Say that again please")
        return "None"
    return query.lower()

def send_email(to, content):
    """Function to send an email"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to, content)
        server.close()
        speak("Email sent successfully")
    except Exception as e:
        logging.error(e)
        speak("Sorry, I failed to send the email")

def remind(message, interval):
    """Function to set a reminder"""
    while True:
        notification.notify(
            title=message,
            message="",
            timeout=20
        )
        time.sleep(interval * 60)

def search_wikipedia(query):
    """Function to search Wikipedia"""
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)
    logging.info(results)

def open_website(url, site_name):
    """Function to open a website"""
    webbrowser.open(url)
    speak(f"Opening {site_name}")

def play_music():
    """Function to play music"""
    songs = os.listdir(MUSIC_DIR)
    os.startfile(os.path.join(MUSIC_DIR, songs[1]))

def tell_time():
    """Function to tell the current time"""
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is: {str_time}")

def open_code():
    """Function to open VS Code"""
    os.startfile(CODE_PATH)

if __name__ == "__main__":
    speak("Hello There!!")
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            search_wikipedia(query)
        elif 'open youtube' in query:
            open_website("https://www.youtube.com/", "YouTube")
        elif 'open google' in query:
            open_website("https://www.google.com/", "Google")
        elif 'open stackoverflow' in query:
            open_website("https://www.stackoverflow.com/", "Stack Overflow")
        elif 'play music' in query:
            play_music()
        elif 'the time' in query:
            tell_time()
        elif 'open code' in query:
            open_code()
        elif 'send email' in query:
            try:
                speak('What shall I say?')
                content = take_command()
                to = "yourmail@gmail.com"
                send_email(to, content)
            except Exception as e:
                logging.error(e)
                speak("Sorry, I failed to send the email")
        elif 'reminder' in query:
            try:
                speak('What shall I remind you about?')
                message = take_command()
                speak('Please mention interval in minutes')
                interval = int(take_command())
                speak("Reminder set successfully")
                remind(message, interval)
            except Exception as e:
                logging.error(e)
                speak("Sorry, I failed to set the reminder")
