import os
import time
import translators as ts
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

r   = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something: ")
        audio   = r.listen(source)
        try:
            text= r.recognize_google(audio)
            a= text
            #print(ts.google(a , to_language = 'bn'))
            x=ts.google(a , to_language = 'bn')
            print(x)
            tts = gTTS(text=x, lang='bn', slow=False)

            filename='new.mp3'
            tts.save(filename)
            playsound(filename)
            os.remove(filename)
            time.sleep(2)
        except:
            print('Unable to recognize.')
            time.sleep(2)

