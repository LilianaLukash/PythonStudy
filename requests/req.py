import random
import requests
G_url = 'https://www.google.com/'
F_url = 'https://www.facebook.com/'
T_url = 'https://twitter.com/'
A_url = 'https://www.amazon.com/'
Ap_url = 'https://www.apple.com/'
urls = [G_url, F_url, T_url, A_url, Ap_url]
a = random.randint(0,4)
res = requests.get(urls[a])
print(res.status_code)
print(res.url)
#print(res.text)
print(len(res.text))

#temperature in your city
city = input('enter your city ')
print(city)
getc = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
cjson = getc.json()
#print(cjson)
clatitude = cjson['results'][0]['latitude']
#print(clatitude)
clongitude = cjson['results'][0]['longitude']
#print(clongitude)
forecast = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={clatitude}&longitude={clongitude}&current_weather=true')
#print(forecast.json())
print(f'Weather today in {city}')
print(forecast.json()['current_weather']['temperature'])

