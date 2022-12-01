from secrets import secrets
import json
import urequests as requests

YOUR_API_KEY = secrets['key']
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Merriam%2C%20KS?unitGroup=us&include=current&key={YOUR_API_KEY}&contentType=json'

def weatherData():    
    response = requests.get(url)
    d = response.json()
    weatherData = []
    weatherData.append({
        'current': {
            'current': round(d['currentConditions']['temp']),
            'max': round(d['days'][0]['tempmax']),
            'min': round(d['days'][0]['tempmin']),
            'conditions': d['days'][0]['conditions'],
            'description': d['days'][0]['description']
            }
        }
    )
    daily = []
    for ea in range(0,5):
        daily.append(
            {
                'datetime': d['days'][ea]['datetime'],
                'tempmax': str(int(round(d['days'][ea]['tempmax'],0))),
                'tempmin': str(int(round(d['days'][ea]['tempmin']))),
                'temp': str(int(round(d['days'][ea]['temp']))),
                'feelslikemax': str(int(round(d['days'][ea]['feelslikemax']))),
                'feelslikemin': str(int(round(d['days'][ea]['feelslikemin']))),
                'feelslike': str(int(round(d['days'][ea]['feelslike']))),
                'precip': d['days'][ea]['precip'],
                'precipprob': d['days'][ea]['precipprob'],
                'preciptype': d['days'][ea]['preciptype'],
                'snow': d['days'][ea]['snow'],
                'snowdepth': d['days'][ea]['snowdepth'],
                'windspeed': d['days'][ea]['windspeed'],
                'cloudcover': d['days'][ea]['cloudcover'],
                'sunrise': d['days'][ea]['sunrise'],
                'sunset': d['days'][ea]['sunset'],
                'moonphase': d['days'][ea]['moonphase'],
                'conditions': d['days'][ea]['conditions'],
                'description': d['days'][ea]['description'],
                'icon': d['days'][ea]['icon']
            }
        )
    weatherData.append({'daily': daily})
    return weatherData

with open('sampleResponse.json', 'w') as f:
    f.write(json.dumps(weatherData()))
f.close()