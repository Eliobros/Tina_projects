import openai
import pyttsx3
import os
import whisper
import speech_recognition as sr


#iniciar a API

openai.api_key = "ggghghghgh"

sem_palavra_ativadora = False
debug_custo = False
debugar = False
#escolher_stt = "whisper"
escolher_stt = "google"
entrada_por_texto = False

#falar ou nao
falar = True

if entrada_por_texto:
    sem_palavra_ativadora = True
    
def generate_answer(messages):
    response = openai.chatCompletion.create(#api antiga
    response = openai.chat.completions.create(##api nova
                       model="gpt-3.5-turbo",
                       messages=messages,
                       temperature=0.5
                     )
    return [response.choises[0].messages]
    )
