import requests

API_KEY = ""  # TODO


LAT_BRUSSELS = 50.8467
LON_BRUSSELS = 4.3525


if __name__ == "__main__":
    print("Fetching weather data for Brussels...")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "lat": LAT_BRUSSELS,
        "lon": LON_BRUSSELS,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=parameters)
    weather_data = response.json()
    try:
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        print(f"Weather in Brussels")
        print(f" - Description: {weather_description}")
        print(f" - Temperature: {temperature} °C\n")
    except KeyError:
        print("Error: Could not retrieve the weather data for")

