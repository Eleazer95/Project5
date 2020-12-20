import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            EleazerX_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            EleazerX_speak("sorry, I did not get that")
        except sr.RequestError:
            EleazerX_speak("sorry, my speech service is down")
        return voice_data

def EleazerX_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def respond(voice_data):
    if "what is your name" in voice_data:
        EleazerX_speak("My name is Eleazar X")
        
    if "who created you" in voice_data:
        EleazerX_speak("A software Engineer named Eleazar created me.")
        
    if "what can you do" in voice_data:
        EleazerX_speak("I can give you accurate advice about anything related to Science")
        
    if "what time is it" in voice_data:
        EleazerX_speak(ctime())
        
    if "search" in voice_data:
    
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        EleazerX_speak("Here is what I found for " + search)
        
    if "what services do you offer" in voice_data:
        EleazerX_speak("we offer the best web services on data analysis and machine learning")
        
    if "when were you created" in voice_data:
        EleazerX_speak("I was created on november fifteen two thousand and twenty")
    
    if "find location" in voice_data:
        location = record_audio("What is the location")
        url = "https://google.nl/maps/place/" + location +"/&amp;"
        webbrowser.get().open(url)
        EleazerX_speak("Here is the location " + location)
        
    if "exit" in voice_data:
        exit()
    
time.sleep(1)        
EleazerX_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
