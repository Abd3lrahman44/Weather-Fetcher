import requests

API_KEY = "a054d069a0ff32005aa59cc3688fb966"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # getting weather description from api
    weather = data["weather"][0]["description"]
    print("Description:", weather)
    # converting temperature to celsius in nearest 2 decimal places
    temperature = data["main"]["temp"] - 273.15
    print("Temperature:", round(temperature,2), "celsius")
    # getting humidity value
    humidity = data["main"]["humidity"]
    print(f"Humidity: {humidity}")
else:
    print("An error occurred.")