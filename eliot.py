import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('ouvindo...')
            voz = audio.listen(source)
            comando = audio.Recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'eliot' in comando:
                comando = comando.replace('eliot', '')
                maquina.say(comando)
                maquina.runAndWait()
           
    except:
        print('Microfone nao esta ok...')
                