import requests
import tkinter as tk

API_KEY = "3c25276d2223bf10a8a31a0c40bf1446"
BASE_URL = "http://api.weatherstack.com/current"

def get_weather():
    city = city_entry.get()
    response = requests.get(BASE_URL, params={"access_key": API_KEY, "query": city})
    weather_data = response.json()
    
    if "current" in weather_data:
        temp = weather_data["current"]["temperature"]
        condition = weather_data["current"]["weather_descriptions"][0]
        result_label.config(text=f"Temperature: {temp}°C\nCondition: {condition}")
    else:
        result_label.config(text="City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()