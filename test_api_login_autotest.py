import requests
import json

with open('creds.json', 'r') as f:
    config = json.load(f)


def test_api_login():

    headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    data = {

    "email": config["email"],
    "password": config["password"]

    }
        
    response = requests.post("https://sandbox.synctoskill.com/api/AccountApi/login", headers=headers, json=data)
    assert response.status_code == 200
    print("status code is:" + str(response.status_code))

    print(response.request.body)
    print(response.json())

    
