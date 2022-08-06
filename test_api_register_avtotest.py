import requests


def test_api_register():

    headers = {
     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    data = {
    
    "password": "Qwer123+",
    "passwordConfirmation": "Qwer123+",
    "email": "mike9238@gmail.com",
    "fullName": "Mike Ser",
    "address": "Lenina 11",
    "phone": "7(926)765-63-70"
  
    }
    
    response = requests.post("https://sandbox.synctoskill.com/api/AccountApi/register", headers=headers, json=data)
    assert response.status_code == 200
    print("status code is:" + str(response.status_code))

    print(response.json())
