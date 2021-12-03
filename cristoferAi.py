import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os

def speak(say):

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 100)
    engine.say(say)
    engine.runAndWait()

def dateTime():
    date_time = datetime.datetime.now().hour
    if date_time < 12:
        speak("Good morning sir\nhow may i help you")
        speak("Tell me password")
    elif date_time == 12 or date_time < 17:
        speak("Good afternoon sir\nhow may i help you")
        speak("Tell me password")
    elif date_time >= 17:
        speak("Good evening sir\nhow may i help you")
        speak("Tell me password")

dateTime()

try:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Password")
        print("*********\n")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, phrase_time_limit=8)
        password = recognizer.recognize_google(audio, language="en-IN")

        if "cristofer" in password:
            speak("now you can use")
            while True:
                recognizer2 = sr.Recognizer()
                with sr.Microphone() as source2:
                    print("Listening.....\n")
                    recognizer2.pause_threshold = 1
                    recognizer2.energy_threshold = 300
                    audio = recognizer2.listen(source2, phrase_time_limit=8)
                    text = recognizer2.recognize_google(audio, language="en-IN")

                if "open google" in text:
                    webbrowser.open_new_tab("https://www.google.com/")

                elif "open youtube" in text:
                    webbrowser.open_new_tab("https://www.youtube.com/")

                elif "open github" in text:
                    webbrowser.open_new_tab("https://github.com/")

                elif "who is sparsh" in text:
                    speak("He is yor friend")

                elif "who is saurav" in text:
                    speak("He is your good friend")

                elif "who are you" in text:
                    speak("Hello! i am cristofer ")

                elif "time please" in text:
                    speak(str(datetime.datetime.now()))

                elif "wikipedia" in text:
                    clear_Text = text.replace("wikipedia", "")
                    result = wikipedia.summary(clear_Text, sentences=3)
                    print(result)
                    speak(result)

                elif "open brave" in text:
                    os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

                elif "open pycharm" in text:
                    os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe")

                elif "open chrome" in text:
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

                elif "play music" in text:
                    os.startfile("E:\\cristofer music")

                elif "stop this" in text:
                    speak("ok\n closing cristofer")
                    break

                elif "your version" in text:
                    speak("one point zero")

                elif "who is your founder" in text:
                    speak("i am created by Mr.Cristofer")

                else:
                    speak("Sorry it is not define yet")
                    print("Error: {Not defined yet}\n")

        else:
            speak("Correct password please")

except Exception as e:
    speak("Speak something")
