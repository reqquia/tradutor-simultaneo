import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator, LANGUAGES
import os

def speak(audio):
    tts = gTTS(text=audio, lang='pt', slow=False)
    tts.save("out.mp3")
    playsound("out.mp3")
    os.remove("out.mp3")

recognizer = sr.Recognizer()
translator = Translator()

try:
    while True:
        with sr.Microphone() as source:
            print("Diga algo em inglês...")
            audio = recognizer.listen(source)

            try:
                print("Reconhecendo...")
                speech_text = recognizer.recognize_google(audio, language="en")
                print(f"Você disse: {speech_text}")

                # Traduzir o texto para português
                translate = translator.translate(speech_text, src='en', dest='pt')
                text_translated = translate.text
                print(f"Tradução: {text_translated}")

                # bot fala o texto traduzido
                speak(text_translated)

            except sr.UnknownValueError:
                print("Não consegui entender o áudio")
            except sr.RequestError as e:
                print(f"Erro ao conectar ao serviço: {e}")

except KeyboardInterrupt:
    print("Programa finalizado.")
