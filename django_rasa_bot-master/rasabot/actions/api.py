import requests
import json

base_url = 'http://127.0.0.1:8000/user/login-api/'

def loginApi(username, password):
    data = {
        "username" : username,
        "password" : password
    }
    headers = {
        "Accept":"*/*",
        "Content-Type":"application/json",
    }
    data = requests.post(base_url, headers=headers, json= data)
    if data.status_code == 200:
        data = json.loads(data.text)
        return data['user_id']
    else:
        return None



print(loginApi('doaa','12345'))