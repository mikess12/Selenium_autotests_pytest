import requests
import json

with open('creds_1.json', 'r') as f:
    config = json.load(f)


def test_api_register():

    headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    data = {

    "password": config["password"],
    "passwordConfirmation": config["passwordConfirmation"],
    "email": config["email"],
    "fullName": config["fullName"],
    "address": config["address"],
    "phone": config["phone"]

    }
        
    response = requests.post("https://synctoskill.com/api/AccountApi/register", headers=headers, json=data)
    assert response.status_code == 200
    print("status code is:" + str(response.status_code))

    print(response.request.body)
    print(response.json())
