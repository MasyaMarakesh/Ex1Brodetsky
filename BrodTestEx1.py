import requests
result = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=32.109333&lon=34.855499&appid=7246520eb610f41bf9f8c056b7f5415f&units=metric')
print('Tel-aviv:',result.json()['main']['temp'])