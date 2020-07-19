import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from clases.python import Python
from sys import exit

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
            anton_speak("No te entiendo, habla mas claro")
        except sr.RequestError:
            anton_speak("Creo que mi servicio se cayo, encargate solo")
        
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
        anton_speak('nos vemos')
        exit()
        
    if 'Cómo' in voice_data:
        if 'python' in voice_data:
            python = Python()
            tipo_respuesta = record_audio('Quieres que te explique con palabras o solo te envio la info')
            time.sleep(1)
            anton_speak(python.recibiendo_pregunta(voice_data,tipo_respuesta))
    

def anton_speak(audio_string):
    tts = gTTS(text=audio_string,lang='es-us')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(1)
anton_speak("Hola")

while 1:
    voice_data = record_audio()
    respond(voice_data)
