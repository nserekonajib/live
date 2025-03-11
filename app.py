from flask import Flask
import requests
import time
import threading

app = Flask(__name__)
API_URL = "https://oga-fx12.onrender.com/api/images"


def keep_api_alive():
    while True:
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                print("API is active:", response.json())
            else:
                print(f"API returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        
        # Wait for 40 seconds before sending the next request
        time.sleep(40)


@app.route('/')
def home():
    return "API Keeper is running!"


if __name__ == "__main__":
    threading.Thread(target=keep_api_alive, daemon=True).start()
    app.run(port=6060, debug=False)
