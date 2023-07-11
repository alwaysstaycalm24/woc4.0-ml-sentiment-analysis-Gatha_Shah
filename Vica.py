from googletrans import Translator
import DesktopApp
import SportsLiveScore
import speech_recognition as sr
import pyttsx3
import WhatsApptext
import webdriver
import datetime
import random
import wikipedia
import webbrowser
# import Mail
import wifi
import time
import weather
import news

voice = pyttsx3.init()
hr = int(datetime.datetime.now().hour)
if 0 <= hr < 12:
    voice.say("Good Morning Gatha")
    voice.runAndWait()
    print("Good Morning Gatha")
elif 12 <= hr < 16:
    voice.say("Good Afternoon Gatha")
    voice.runAndWait()
    print("Good Afternoon Gatha")
elif 16 <= hr < 21:
    voice.say("Good Evening Gatha")
    voice.runAndWait()
    print("Good Evening Gatha")

assname = "Boomer 2 point o"
voice.say("I am your Assistant")
voice.say(assname)
voice.runAndWait()

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        try:
            text = r.recognize(audio)
            print(f"You Said :{text}\n")
            if "weather" in text.lower():
                weather.weatherupdate()

            elif "good morning" in text.lower():
                time.time()
                time.date()
                time.day()
                weather.weatherupdate()
                print("Todays Headlines")
                voice.say("todays headlines")
                voice.runAndWait()
                news.news()
                print("Have a Fantastic Day")
                voice.say("Have a fantastic day")
                voice.runAndWait()

            elif "introduce" in text.lower():
                print("Hey i'm Boomer two point o your assistant \n How may i help you!")
                voice.say("Hey i'm Boomer two point o your assistant \n How may i help you!")
                voice.runAndWait()

            elif "who made you" in text.lower() or "who created you" in text.lower():
                print("By Gatha")
                voice.say("I have been created by Gatha.")
                voice.runAndWait()

            elif "who i am" in text.lower():
                voice.say("If you talk then definitely your human.")

            elif "set alarm" in text.lower():
                voice.say("closing clock and alarm")
                import Alarm

                voice.runAndWait()
                continue

            elif "stopwatch" in text.lower():
                voice.say("opening stopwatch")
                import stopwatch

                voice.runAndWait()

            elif "translate" in text.lower():
                # translator = Translator(service_urls=["translate.google.com"])
                # translation1 = translator.translate(text, dest="hi")
                # print(f"Translated into Hindi :{translation1.text}\n")
                # voice.say("Sorry i cannot speak hindi")
                voice.say("opening translator")
                import langtrans

                voice.runAndWait()
                continue

            elif "convert" in text.lower():
                import sample

                voice.say("opening voice translator")

                voice.runAndWait()

            elif "whatsapp" in text.lower():
                voice.say("Scan QR code with your phone")
                voice.say("opening whatsapp : ")
                voice.runAndWait()
                WhatsApptext.msg()

            elif "open Sports" in text.lower():
                SportsLiveScore.live()

            elif "open calculator" in text.lower():
                print("Opening Calculator")
                voice.say("opening calculator")
                voice.runAndWait()
                DesktopApp.calculator()
            elif "open cmd" in text.lower():
                DesktopApp.cmd()
                print("Opening CMD")
                voice.say("opening cmd")
                voice.runAndWait()
            elif "open character map" in text.lower():
                print("Opening CharacterMap")
                voice.say("opening charactermap")
                voice.runAndWait()
                DesktopApp.character_map()
            elif "open con" in text.lower():
                print("Opening Console")
                voice.say("opening console")
                voice.runAndWait()
                DesktopApp.console()
            elif "open control panel" in text.lower():
                print("Opening Control Panel")
                voice.say("opening control panel")
                voice.runAndWait()
                DesktopApp.control_panel()
            elif "open paint" in text.lower():
                print("Opening Paint")
                voice.say("opening paint")
                voice.runAndWait()
                DesktopApp.paint()
            elif "open Notepad" in text.lower():
                print("Opening Notepad")
                voice.say("opening notepad")
                voice.runAndWait()
                DesktopApp.notepad()
            elif "open task manager" in text.lower():
                print("Opening TaskManager")
                voice.say("opening task manager")
                voice.runAndWait()
                DesktopApp.taskmanager()
            elif "open android's" in text.lower():
                print("Opening Android studio")
                voice.say("opening android studio")
                voice.runAndWait()
                DesktopApp.androidstudio()

            elif "google" in text.lower():
                voice.say("opening google")
                voice.runAndWait()
                webdriver.google()
            elif "gmail" in text.lower():
                voice.say("opening gmail")
                voice.runAndWait()
                webdriver.gmail()
            elif "yahoo mail" in text.lower():
                voice.say("opening yahoo mail")
                voice.runAndWait()
                webdriver.yahoomail()
            elif "drive" in text.lower():
                voice.say("opening drive")
                voice.runAndWait()
                webdriver.drive()
            elif "twitter" in text.lower():
                voice.say("opening twitter")
                voice.runAndWait()
                webdriver.twitter()
            elif "facebook" in text.lower():
                voice.say("opening facebook")
                voice.runAndWait()
                webdriver.facebook()
            elif "instagram" in text.lower():
                voice.say("opening instagram")
                voice.runAndWait()
                webdriver.instagram()
            elif "youtube" in text.lower():
                voice.say("opening youtube")
                voice.runAndWait()
                webdriver.youtube()
            elif "amazon" in text.lower():
                voice.say("opening amazon")
                voice.runAndWait()
                webdriver.amazon()
            elif "flipkart" in text.lower():
                voice.say("opening flipkart")
                voice.runAndWait()
                webdriver.flipkart()
            elif "discord" in text.lower():
                voice.say("opening discord")
                voice.runAndWait()
                webdriver.discord()
            elif "dropbox" in text.lower():
                voice.say("opening dropbox")
                voice.runAndWait()
                webdriver.dropbox()

            elif "time" in text.lower():
                x = datetime.datetime.now()
                voice.say(x)
                voice.runAndWait()
                print(x)
            elif "news" in text.lower():
                news.news()

            elif "joke" in text.lower():
                a = "I love how in horror movies the person calls out, HELLO? \n As if the ghost will Answer,Hey, " \
                    "what's up, I'm in the kitchen. Want a sandwich?👻💀 "
                b = "What did one shark say to the other while eating a clownfish? \n This tastes funny🐠"
                c = "What movie should you watch on a dinner date?🍴 \n Kabhi Sushi Kabhie Rum 🌭🥂"
                d = "What do you call a rose that wants to go to the moon?🌹🌚 \n Gulab Ja Moon 😂😂"
                e = "What movie does the hopeless clock?⏰ \n Kal Ho Na Ho ⌛⏳ "
                list1 = [a, b, c, d, e]
                x = (random.choice(list1))
                print(x)
                voice.say(x)
                voice.runAndWait()

            elif "song" in text.lower():
                voice.say("opening spotify")
                voice.runAndWait()
                webdriver.spotify()

            elif "wikipedia" in text.lower():
                voice.say("Searching Wikipedia")
                text = text.replace("wikipedia", "")
                results = wikipedia.summary(text, sentences=2)
                voice.say(results)
                print(results)
                voice.runAndWait()

            elif 'search' in text.lower() or 'play' in text.lower():
                text = text.replace("search", "")
                text = text.replace("play", "")
                webbrowser.open(text)

            elif "mail" in text.lower():
                voice.say("sending")
                import Mail

                voice.runAndWait()

            elif "on" and "Wi-Fi" in text.lower():
                wifi.on()
            elif "off" or "of" and "Wi-Fi" in text.lower():
                wifi.off()

            elif "see you soon" in text.lower():
                print("Quiting Session!!!")
                break

            else:
                voice.say("Error")
                voice.runAndWait()
                print("Error")

        except:
            print("Sorry Dude couldn't get that")
            voice.say("sorry dude couldn't get that")
            voice.runAndWait()
