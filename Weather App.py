import requests

def get_weather(city):
    base_url = "https://ms-tech.stoplight.io/mocks/ms-tech/weather-app/111233/weather" #change init on your way
    params = {
        "city": city
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        # API response structure ke hisaab se fields access karein
        weather_desc = data.get('description', 'No description').capitalize()
        temp = data.get('temperature', 'N/A')
        humidity = data.get('humidity', 'N/A')
        print(f"Weather in {city}: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("City not found. Please check the city name.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()