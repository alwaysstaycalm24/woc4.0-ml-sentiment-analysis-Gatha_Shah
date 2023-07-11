import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("shahgatha214@gmail.com", "compceo@#")
server.sendmail("shahgatha214@gmail.com",
                "shahgatha214@gmail.com",
                "Respected Charmy Ma'am,"
                "\n\nMy name is Gatha Shah and I am contacting you to talk about project, it shows"
                "too many errors.I appreciate if we can meet at a mutually convenient time to talk about "
                "error/topics.\n\nThank you for your consideration and your time. I am looking forward to meet you."
                "\n\nBest Regards""\nGatha")

server.quit()



"""import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

    import ezgmail
import speech_recognition as sr
import pyttsx3


def mail():
    voice1 = pyttsx3.init()
    r = sr.Recognizer()
    voice1.say("Sorry you will have to enter the Email address manually")
    voice1.say("Enter recipient")
    voice1.runAndWait()
    recipient = input("Enter Recipient :")
    with sr.Microphone() as source1:
        print("Enter Email Subject:")
        voice1.say("Enter Email Subject")
        voice1.runAndWait()
        audio1 = r.listen(source1)
        try:
            text1 = r.recognize(audio1)
            print(f"Subject :{text1}\n")
            subject = text1
            with sr.Microphone() as source2:
                print("Compose Email: ")
                voice1.say('compose mail')
                voice1.runAndWait()
                audio2 = r.listen(source2)
                try:
                    text2 = r.recognize(audio2)
                    print(f"Text :{text2}\n")
                    text0 = text2

                    ezgmail.send(recipient, subject, text0)

                except:
                    print("Error")
                    voice1.say("error")
                    voice1.runAndWait()

        except:
            print("Error")
            voice1.say("error")
            voice1.runAndWait()"""

