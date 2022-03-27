import requests
import json


def loginApi(username, password):
    base_url = 'http://127.0.0.1:8000/user/login-api/'
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


if __name__ == "__main__":
    print(loginApi('doaa','12345'))






def degreeApi(course_name, user_id):
    base_url = 'http://127.0.0.1:8000/university/degree-api/'
    data = {
        "course_name" : course_name,
        "user_id" : user_id
    }
    headers = {
        "Accept":"*/*",
        "Content-Type":"application/json",
    }
    data = requests.post(base_url, headers=headers, json= data)
    if data.status_code == 200:
        data = json.loads(data.text)
        return data['degree']
    else:
        return None


if __name__ == "__main__":
    print(degreeApi('Machine Learning','2'))