# import googletrans
# print(googletrans.LANGCODES)

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog1 = spr.Recognizer()
mc = spr.Microphone()

with mc as source:
    print("Speak 'hello' to initiate the Translation !!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    recog1.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog1.listen(source)
    MyText = recog1.recognize(audio)
    MyText = MyText.lower()

if 'hello' in MyText:
    translator = Translator()
    from_lang = 'en'
    to_lang = 'hi'

    with mc as source:
        print("Speak a Sentence..!")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        get_sentence = recog1.recognize(audio)

        try:
            print("Phase to be Translated:" + get_sentence)
            text_to_translate = translator.translate(get_sentence, src= from_lang, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow=False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")

        except:
            print("Unable to Understand the Input")




from google_trans_new import google_translator
import streamlit as st
translator = google_translator()
st.title("Language Translator")
text = st.text_input("Enter a text")
translate = translator.translate(text, lang_tgt='hi')
st.write(translate)