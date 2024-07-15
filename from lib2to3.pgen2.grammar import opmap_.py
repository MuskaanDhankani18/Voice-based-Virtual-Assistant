from lib2to3.pgen2.grammar import opmap_raw
import operator
from pdb import pm
import speech_recognition as sr   # to recognise voice
# from playsound import playsound                       # to play audio
import random
from gtts import gTTS                  # google text to speech
import webbrowser                      # to open browser
import ssl 
import certifi 
import time
import os                              # to remove the audio files 
import subprocess
from PIL import Image
import pyautogui                       # screenshot
import pyttsx3
import bs4 as bs 
import urllib.request
import sounddevice
import pyaudio
import threading

class TimerEvent:
    def __init__(self, time):
        def __init__(self, seconds:int):
            """
            time = time in seconds
            """
        self.time = time
        self.status = True # stores whether or not to continue the timer
        # self.seconds = seconds

    def start(self):
        self.status = True # stores whether or not to continue the timer
        self.timer_thread = threading.Thread(target=self.countdown)
        self.timer_thread.start()

    def stop(self):    
        def pause(self):
            self.status = False

    def countdown(self):
        while (self.status and self.time):
            self.time -= 1
        while (self.status and self.seconds):
            self.seconds -= 1
            time.sleep(1)

        # if the time is zero
        if (not self.time):
            if (not self.seconds):
                print("timer over")

x = TimerEvent(10)
x.start()
print("other stuff")
x.stop()
# testing
if __name__ == "__main__":
    x = TimerEvent(10)
    x.start()
    print("other stuff")
    x.stop()

class Person:
    name = ''
    def setName(self,name):
        self.name = name

class Assist:
    name = ''
    def setName(self,name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()                    # initialise the recognizer
# listen for audio and convert it to text

def record_audio(ask = ""):
    with sr.Microphone() as source:    # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for audio via source
        print("Done Listening")
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)   # convert audio to text
        except sr.UnknownValueError:        # error:recogniser doesn't understand
            engine_speak("Sorry Sir, I didn't get it")
        except sr.RequestError:
            engine_speak("Sorry, the server is down")  # error:the recogniser is not connected
            print(">>",voice_data.lower())   # print what the user said
            return voice_data.lower()

# get string and make audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech
    r = random.randint(1,20000000)
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    #playsound.playsound(audio_file) # help us to play the audio
    print(Assist_obj.name+ ":",audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file

def respond(voice_data):
    #1. greeting
    if there_exists(['Hello,Hi,Hey,Hey Boss,Hola']):
        greetings = ['Hey, How can I help you'+ Person_obj.name, 'How can I help you'+ Person_obj.name, 'Hello'+ Person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    #2. name
    if there_exists("What is your name ?","Tell me your name"):
        if Person_obj.name:
            engine_speak("I don't know my name, please give my name by saying command your name should be ,,,, What is your name")
        else:
            engine_speak("What's your name sir")

    if there_exists(["My name is"]):
        Person_name = voice_data.split("is")[-1].strip()
        engine_speak("Okay sir, I'll remember that your name is "+Person_name())
        Person_obj.setName(Person_name)  # remember name in person object

    if there_exists(["Your name should be "]):
        Assist_name = voice_data.split("be")[-1].strip()
        engine_speak("Okay I'll remember that my name is "+Assist_name)
        Assist_obj.setName(Assist_name)  # remember name in person object

    #3. greetings 
    if there_exists(["How are you","How are you doing"]):
        engine_speak("I'm very well, thanks for asking"+Person_obj.name)

    #4. time
    if there_exists(["What's the time","tell me the time","time please"]):
        time = time().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
            minutes = time[1]
            time = hours + "hours and" + minutes +"minutes"
            engine_speak(time)

    #5. search google
    if there_exists(["Search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url="https://google.com/search?q" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    #6. search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on youtube")

    #7. get to know the stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on youtube")

    #8. search for music
    if there_exists(["play music"]):
        search_term = voice_data.split("for")[-1]
        url = "https://open.spotify.com/search/" + search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to" + search_term + "enjoy your favourite") 

    #9. search for amazon
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.amazon.in" + search_term
        webbrowser.get().open(url)
        engine_speak("Here us what I found for" + search_term + " on amazon.com")

    #10. make a note
    if there_exists(["make a note"]):
        search_term = voice_data.split("for")[-1]
        url = "https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")

    #11. open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("Opening instagram")

    #11. open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("Opening instagram")

    #11. open twitter
    if there_exists(["open twitter"]):
        search_term = voice_data.split("for")[-1]
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("Opening twitter")  

    #12. time table 
    if there_exists(["show my time table"]):
        im = Image.open()
        im.show()

    #13. weather
    if there_exists(["Weather","tell me the weather report","what's the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    #14. open gmail 
    if there_exists(["Open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("Here you can check your gmail")

    #15. game ----- stone, paper, scissor -----
    if there_exists(["Game"]):
        voice_data = record_audio("Choose among rock, paper or scissor")
        moves = ["rock","paper","scissor"]
        cmove = random.choice(moves) 
        pmove = voice_data
        engine_speak("The computer chooses" + cmove)

        if pmove == cmove:
            engine_speak("The match draw")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

    #16. toss a coin
    if there_exists(["toss","flip","coin"]):
        moves = ["head","tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chooses" + cmove) 

    #17. calculator
    if there_exists(["add","subtract","multiply","divide","power","+","-","","/","*"]):
        opr = voice_data.split()[1]
        if opr == "Add":
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == "Subtract":
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == "Multiply":
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == "Divide":
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))        
        elif opr == "Power":
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong operator")

    #18. screenshot
    if there_exists(["Capture","screenshot","my screen"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('')


time.sleep(1)
Assist_obj = Assist()
Person_obj = Person()
Assist_obj.name = 'Jarvis'
engine = pyttsx3.init()

while(1):
    voice_data = record_audio("Recording")  # get the voice input
    print("Done")
    print("Ques : ",voice_data)
    respond(voice_data)  # respond