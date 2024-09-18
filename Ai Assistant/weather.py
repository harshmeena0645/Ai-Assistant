from requests_html import HTMLSession                     #install in Visual : pip install requests-html
import speech_to_text                                   #install in Visual : pip install lxml



import requests

def weather(city="jaipur"):
    api_key = "26af18538d2dc65a06bc17163ee92e86"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"{temp}°C {desc}"
    else:
        return "Weather information could not be retrieved"

print(weather())
