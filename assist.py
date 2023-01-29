import os  # pip install os
from plyer import notification  # pip install plyer
import smtplib  # pip install smtplib
import speech_recognition as sr  # pip install speechRecognition
import pyttsx3  # pip install pyttsx3
import pyaudio  # pip install pyaudio
import datetime  # pip install datetime
import wikipedia  # pip install wikipedia
import webbrowser # pip install webbrowser
import time
'''
initiating speech of the assistant
'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


'''
Functions defined for the assistant 
'''


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am your assistant your exilency, Please tell me how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Example@gmail.com', 'Password')
    server.sendmail('jkartik156@gmail.com', to, content)
    server.close()


def remind(Message, Interval):
    while True:
        notification.notify(
            title=f"{Message}",
            message=f"",
            timeout=20
        )
        time.sleep(Interval*60)


'''
Execution of speech recognition and the following commands
'''

if __name__ == "__main__":
    speak("Hello There!!")
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening!")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Opening!")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")
            speak("Opening!")

        elif 'play music' in query:
            music_dir = "C:\\Users\\jkart\\OneDrive\\Desktop\\gud"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            # Logic for executing commands

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is: {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\jkart\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('what shall i say?')
                content = takeCommand()
                to = "jkartik156@gmail.com"
                sendEmail(to, content)
                speak("Email sent sucessfully")
            except Exception as e:
                print(e)
                speak("Sorry , I failed , I shall go die now ;-;")

        elif 'reminder' in query:
            try:
                speak('what shall i remind you about?')
                Message = takeCommand()
                speak('Please mention interval in minutes')
                Interval = takeCommand()
                speak("Remainder set sucessfully")
                remind(Message, Interval)
            except Exception as e:
                print(e)
                speak("Sorry , I failed , I shall go die now ;-;")
