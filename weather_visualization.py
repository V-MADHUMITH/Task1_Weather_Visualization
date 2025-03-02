import requests

# Replace with your actual API key
API_KEY = "098688648b2b72ca56cb9e53b08cae59"  

# List of cities
cities = ["London", "New York", "Tokyo", "Paris", "Mumbai"]

# Function to fetch weather data
def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
    else:
        print(f"Failed to fetch data for {city}")
        return None

# Fetch weather data for all cities
weather_data = [fetch_weather(city) for city in cities if fetch_weather(city)]

# Print the results
for entry in weather_data:
    print(entry)



    import matplotlib.pyplot as plt
import seaborn as sns

# Extract data for visualization
city_names = [entry["City"] for entry in weather_data]
temperatures = [entry["Temperature"] for entry in weather_data]
humidity = [entry["Humidity"] for entry in weather_data]

# Set plot style
sns.set_theme(style="whitegrid")

# Plot Temperature Comparison
plt.figure(figsize=(8,5))
sns.barplot(x=city_names, y=temperatures, palette="coolwarm")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperature in Different Cities")
plt.show()

# Plot Humidity Comparison
plt.figure(figsize=(8,5))
sns.barplot(x=city_names, y=humidity, palette="Blues")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.title("Humidity Levels in Different Cities")
plt.show()


