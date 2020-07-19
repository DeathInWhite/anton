import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:

        if ask:
            anton_speak(ask)

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio,language="es-ES")
        except sr.UnknownValueError:
            anton_speak("Sorry, I Did not get that")
        except sr.RequestError:
            anton_speak("Sorry, my speech service is down")
        
        return voice_data


def respond(voice_data):
    if 'Cuál es tu nombre' in voice_data:
        anton_speak("Que te importa ahueonao")
    if 'qué hora es' in voice_data:
        anton_speak(ctime())
    if 'busca' in voice_data:
        busqueda = record_audio('Que es lo que quieres que busque por ti weon flojo?')
        url = 'https://google.com/search?q='+busqueda
        webbrowser.get().open(url)
        anton_speak('esto es lo que encontre de la busqueda' + busqueda)
    if 'encuentra un lugar' in voice_data:
        busqueda = record_audio('Que lugar quieres buscar?')
        url = 'https://google.nl/maps/place/'+busqueda+'/&amp'
        webbrowser.get().open(url)
        anton_speak('esto encontre por tu busqueda de '+ busqueda)
    if 'termina' in voice_data:
        exit()
    

def anton_speak(audio_string):
    tts = gTTS(text=audio_string,lang='es-us')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(1)
anton_speak("Que huea quieres ahora??")

while 1:
    voice_data = record_audio()
    respond(voice_data)