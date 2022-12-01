import requests
import json
from appInfo import appData

def access_token():
    url = 'https://api.honeywell.com/oauth2/accesstoken'
    header = {'Authorization': appData['auth']}
    body = {'grant_type': 'client_credentials'}
    response = requests.post(url,headers = header, data = body)
    access_token = f"Bearer {json.loads(response.content)['access_token']}"
    return json.loads(response.content)