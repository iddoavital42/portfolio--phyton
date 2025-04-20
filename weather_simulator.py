import tkinter as tk
import random

def generate_weather(city):
    temperature = round(random.uniform(-5, 40), 1)
    humidity = random.randint(20, 100)
    wind_speed = random.randint(0, 40)
    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Stormy", "Snowy", "Foggy"]
    condition = random.choice(conditions)

    return {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "condition": condition
    }

def show_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city.")
        return

    weather = generate_weather(city)
    result = (
        f"📍 City: {weather['city']}\n"
        f"🌡️ Temperature: {weather['temperature']}°C\n"
        f"💧 Humidity: {weather['humidity']}%\n"
        f"🌬️ Wind: {weather['wind_speed']} km/h\n"
        f"🌤️ Condition: {weather['condition']}"
    )
    result_label.config(text=result)

# 🪟 GUI
root = tk.Tk()
root.title("Weather Simulator")
root.geometry("400x300")

tk.Label(root, text="Enter a city:").pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
