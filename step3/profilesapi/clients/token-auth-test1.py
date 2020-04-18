import requests

def client():
    # credentials = {"username": "admin", "password": "xxxx"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    token_h = "Token 48d62c8648af60eb7870efd4b06655bdc79286ab"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()
