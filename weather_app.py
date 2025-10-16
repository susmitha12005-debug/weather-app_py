import requests
from tkinter import *

# Function to get weather
def get_weather():
    city = city_entry.get()
    api_key = "ddddc1cde683dad8d685b4ef072e5f41"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        weather_label.config(text="City not found!")
        return

    temp = response['main']['temp']
    weather_desc = response['weather'][0]['description']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']

    weather_info = f"Temperature: {temp}°C\nWeather: {weather_desc}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
    weather_label.config(text=weather_info)

# GUI setup
root = Tk()
root.title("Weather App")
root.geometry("400x300")

city_entry = Entry(root, width=30)
city_entry.pack(pady=20)

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = Label(root, text="", font=("Helvetica", 12))
weather_label.pack(pady=20)

root.mainloop()
