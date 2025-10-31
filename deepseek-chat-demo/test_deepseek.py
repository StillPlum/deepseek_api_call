import requests

URL = "http://127.0.0.1:7860/chat"

if __name__ == "__main__":
    r = requests.post(URL, json={"user_id": "u1", "message": "Hello DeepSeek"})
    print(r.status_code, r.json())
