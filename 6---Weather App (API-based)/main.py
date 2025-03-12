import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_weather(city, api_key):
    """
    Fetches weather details for the specified city using the OpenWeatherMap API.

    Parameters:
    city (str): Name of the city.
    api_key (str): Your OpenWeatherMap API key.

    Returns:
    dict: Weather details including temperature, humidity, and description.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        weather_details = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].capitalize(),
            'icon': get_weather_icon(data['weather'][0]['main'])
        }
        return weather_details

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching weather data: {e}")
        return None
    except KeyError:
        print(Fore.RED + "Unexpected response format.")
        return None

def get_weather_icon(condition):
    """
    Maps weather conditions to corresponding emojis.

    Parameters:
    condition (str): Weather condition from the API.

    Returns:
    str: Emoji representing the weather condition.
    """
    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Haze": "🌫️",
        "Fog": "🌫️"
    }
    return icons.get(condition, "🌍")  # Default icon

def display_weather(city, weather_details):
    """
    Displays the weather details for the specified city.

    Parameters:
    city (str): Name of the city.
    weather_details (dict): Weather details to display.
    """
    if weather_details:
        print(Fore.CYAN + Style.BRIGHT + f"\nWeather in {city.capitalize()} 🌆:")
        print(Fore.YELLOW + f"Temperature: {weather_details['temperature']}°C {weather_details['icon']}")
        print(Fore.GREEN + f"Humidity: {weather_details['humidity']}%")
        print(Fore.MAGENTA + f"Condition: {weather_details['description']}")
    else:
        print(Fore.RED + f"\nCould not retrieve weather details for {city}. Please check the city name.")

if __name__ == "__main__":
    api_key = "0531e966e7404bb50f3d914b8c5e47b8"  
    print(Fore.CYAN + "🌟 Welcome to the Weather App 🌟")
    city = input(Fore.BLUE + "Enter the city name: ")
    weather_details = get_weather(city, api_key)
    display_weather(city, weather_details)

