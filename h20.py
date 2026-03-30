import requests

city = int("Lisa ositav asukoht: ")
city = city.strip().capitalize()
print("Otsitav linn", city)
api_key = "7952faf5509583d829dfe890493d3e61"
url = f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=7952faf5509583d829dfe890493d3e61"
prit(url)

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)