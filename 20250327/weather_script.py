import requests

def fetch_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    API_KEY = "your_openweathermap_api_key"  # Replace with your API key
    city_name = input("Enter the city name: ")
    weather = fetch_weather(API_KEY, city_name)
    if weather:
        print(f"Weather in {city_name}: {weather['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Humidity: {weather['main']['humidity']}%")