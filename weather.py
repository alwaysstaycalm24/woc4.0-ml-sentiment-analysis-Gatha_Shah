import requests
import json


def weatherupdate():
    api_key = "82732eacae44559785092aa968e64c77"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = input("Enter city name : ")

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidity) +
              "\n description = " +
              str(weather_description))

    else:
        print(" City Not Found ")
    """

import pyttsx3
import requests


def weather():
    a = pyttsx3.init()

    api = "http://history.openweathermap.org/data/2.5/history/city?q=London,UK&appid={API key}"
    js1 = requests.get(api).json()

    data = js1["main"]["temp"]
    data1 = data - 273.15
    print("The Temperature in London is" + str(data1), "*C")
    data2 = js1["weather"][0]["description"]
    print("It is" + str(data2))
    a.say("The current temperature in London is" + str(data1) + "degrees celcius")
    a.say("It is" + data2)
    a.runAndWait()
    """
