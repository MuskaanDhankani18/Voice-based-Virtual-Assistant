import speech_recognition as sr #convert speech to text
from time import time,ctime
import os
from gtts import gTTS
import datetime
import pyjokes
import pyaudio
import playsound
from wikipedia import *
import webbrowser
from googletrans import Translator
import pywhatkit

def talk():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something....") 
        r.pause_threshold=1
        audio=r.listen(source,0,8)
        data=""
    try:
        print("Recognizing...")
        data=r.recognize_google(audio)
        print("You said, " + data)
    except Exception as e:
        print("Could not understand audio"+ str(e))
    return data

def speak(text):
    print(text)
    response=gTTS(text=text, lang='en')
    file = "voice.mp3"
    try:
        os.remove(file)
    except OSError:
        pass
    response.save(file)
    playsound.playsound(file)

'''def WishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good Morning!!")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    speak("I am Jarvis.Please tell me how may I help you!")  '''    

while(True):
    text=talk().lower()

    if "time" in text:
        speak(ctime())
    elif 'youtube' in text:
        speak("Opening YouTube....")
        webbrowser.open_new_tab("http://www.youtube.com")
    elif 'search' in text:
        text = text.replace("search", "")
        webbrowser.open_new_tab(text)
        time.sleep(10)
    elif 'open google' in text:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google is open")
        time.sleep(5)   
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    elif "whatsapp" in text:
                msg = text.replace("whatsapp", "")
                pywhatkit.sendwhatmsg_instantly("+917974759467","Bye diyu")
                print("Successfully Sent!")
                speak("successfully sent")
    if "play" in text:
                song = text.replace("play", "")
                speak("playing" + song)
                pywhatkit.playonyt(song)
    elif 'exit' in text:
        speak("GoodBye...Till next time")
        exit()


