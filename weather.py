import requests
import json
from config import token_weather

from pprint import pprint                              #  ВРЕМЕННО

class Weather():

    city = "Achinsk,RU" 

    def __init__(self):
        self.url_like = "http://api.openweathermap.org/data/2.5/find"
        self.url_forecast = "http://api.openweathermap.org/data/2.5/forecast"
        self.params = {
            "q": self.city,
            "type": "like",
            "units": "metric",
            "lang": "ru",
            "APPID": token_weather
            }

    def get_weather_like(self):
        response = requests.get(url=self.url_like, params=self.params)
        raw_weather = response.json()

        weather_like = dict()
        date = raw_weather["list"][0]
        weather_like["city"] = date["name"]
        weather_like["temp"] = round(date["main"]["temp"])
        weather_like["feels_like"] = round(date["main"]["feels_like"])
        weather_like["description"] = date["weather"][0]["description"]
        weather_like["snow"] = date["snow"]
        weather_like["rain"] = date["rain"]
        weather_like["wind_speed"] = str(round(date["wind"]["speed"])) + " м/с."
        
        return weather_like

    def get_weather_forecast(self):
        response = requests.get(url=self.url_forecast, params=self.params)
        raw_weather = response.json()

        weather_forecast = dict()
        weather_forecast["city"] = raw_weather["city"]["name"]
        weather_forecast["date"] = list()
        for time in raw_weather["list"]:
            buffer = dict()
            buffer["time"] = time["dt_txt"]
            buffer["temp"] = round(time["main"]["temp"])
            buffer["feels_like"] = round(time["main"]["feels_like"])
            buffer["description"] = time["weather"][0]["description"]
            buffer["wind_speed"] = str(round(time["wind"]["speed"])) + " м/с."
            weather_forecast["date"].append(buffer)
    
        return weather_forecast

    def print(self, date):                              #  ВРЕМЕННО
        pprint(date)


weather = Weather()
date = weather.get_weather_like()
weather.print(date)
