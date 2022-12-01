from secrets import secrets
import urequests as requests

YOUR_API_KEY = secrets['key']
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Merriam%2C%20KS?unitGroup=us&include=current&key={YOUR_API_KEY}&contentType=json'

def weatherData():    
    response = requests.get(url)
    d = response.json()

    current = round(d['currentConditions']['temp'])
    max = round(d['days'][0]['tempmax'])
    min = round(d['days'][0]['tempmin'])
    conditions = d['days'][0]['conditions']
    description = d['days'][0]['description']

    deg = u'\u00b0'
    c, mx, mn = len(str(current)), len(str(max)), len(str(min))
    space = 9-c-mx-mn
    topRow = f"T:{current}{' '*space}H:{max} L:{min}"
    bottomRow = f"{conditions} - {description}"
    return topRow, bottomRow