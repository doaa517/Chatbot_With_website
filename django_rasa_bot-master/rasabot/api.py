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

def degreeApi(course_name, user_id):
    """_summary_
    
    Args:
        course_name (str): _description_
        user_id (str): _description_

    Returns:
        student_id: str
        course_name: str
        degree: float 
    """
    base_url = 'http://127.0.0.1:8000/university/degree-api/'
    data = {
        "course_name" : course_name,
        "user_id" : user_id
    }
    headers = {
        "Accept":"*/*",
        "Content-Type":"application/json",
    }
    data = requests.get(base_url, headers=headers, json= data)
    if data.status_code == 200:
        data = json.loads(data.text)
    
        return data['student'], data['course_name'], data['degree']
    else:
        return None

def classInfoApi(course_name):
    """_summary_
    
    Args:
        course_name (str): _description_
        
    Returns:
    course_title: str
    class_title: str
    class_day: str
    start_time: str
    end_time: str
    lecturer: str
}
    """
    base_url = 'http://127.0.0.1:8000/university/class-info-api/'
    data = {
        "course_name" : course_name,
    }
    headers = {
        "Accept":"*/*",
        "Content-Type":"application/json",
    }
    data = requests.get(base_url, headers=headers, json= data)
    if data.status_code == 200:
        data = json.loads(data.text)

        return data['course_title'], data['class_title'], data['class_day'], data['start_time'], data['end_time'], data['lecturer']
    else:
        return None


if __name__ == "__main__":
    print(classInfoApi('arabic'))