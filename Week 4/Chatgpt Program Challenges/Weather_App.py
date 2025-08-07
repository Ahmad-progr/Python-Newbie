import requests
import sys


def main():
    temp, feels_like, humidity, condition, city, country = conversion()

    print("\n🌤️  Weather Report")
    print("-" * 30)
    print(f"🏙️  Location        : {city}")
    print(f"🌍 Country         : {country}")
    print(f"🌡️  Temperature     : {temp:.1f}°C")
    print(f"🤒 Feels Like      : {feels_like:.1f}°C")
    print(f"💧 Humidity        : {humidity}%")
    print(f"⛅ Condition       : {condition}")
    print("-" * 30)


def get_weather():
    while True:
        city = input("Enter city name: ").strip()
        try:
            response = requests.get(
                f"YOUR OPENWEATHER API"
            )
            data = response.json()

            if data.get("cod") != 200:
                print("City not found. Please try again.\n")
                continue
            return data
            

        except requests.exceptions.RequestException:
            sys.exit("Network error. Could not complete your request.")


def get_attributes():
    weather_data = get_weather()
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["main"].capitalize()
    feels_like = weather_data["main"]["feels_like"]
    country = weather_data["sys"]["country"]
    city = weather_data["name"]

    return temp, condition, humidity, feels_like, city, country


def conversion():
    temp, condition, humidity, feels_like, city, country = get_attributes()
    temp_c = float(temp) - 273.15
    feels_like_c = float(feels_like) - 273.15
    return temp_c, feels_like_c, humidity, condition, city, country


if __name__ == "__main__":
    main()
