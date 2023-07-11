import datetime
import pyttsx3

voice = pyttsx3.init()
j = datetime.datetime.now()


def time():
    x = j.strftime("%I")
    y = j.strftime("%M")
    z = j.strftime("%P")
    time1 = (str(x) + str(y) + str(z))
    print("The Time is " + str(time1))
    voice.say("The time is")
    voice.say(time1)
    voice.runAndWait()


def month():
    x = j.strftime("%B")
    print("The month is " + str(x))
    voice.say("The Month is")
    voice.say(x)
    voice.runAndWait()


def year():
    x = j.strftime("%Y")
    print("The year is " + str(x))
    voice.say("The year is")
    voice.say(x)
    voice.runAndWait()


def date():
    x = j.strftime("%d")
    y = j.strftime("%B")
    print("Today's Date is " + str(x) + " " + str(y))
    voice.say(x)
    voice.say(y)
    voice.runAndWait()


def day():
    x = j.strftime("%A")
    print("The day is " + str(x))
    voice.say("The day is " + str(x))
    voice.runAndWait()
