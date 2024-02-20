import requests
import json
import pyttsx3

text_speech = pyttsx3.init()

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=8b6dd7dab9494e8ea9b190336241202&q={city}"

r = requests.get(url)


wdic = json.loads(r.text)

w = wdic["current"]["temp_c"]
f = wdic["current"]["feelslike_c"]
h = wdic["current"]["humidity"]
d = wdic["current"]["condition"]["text"]

print(f"The current weather in {city} is {w} degrees Celsius , but it feels like {f} degree celsius, The humidity is {h} percent, and it is {d} in {city}")

text_speech.say(f"The current weather in {city} is {w} degrees Celsius , but it feels like {f} degree celsius, The humidity is {h} percent, and it is {d} in {city}")
text_speech.runAndWait()
