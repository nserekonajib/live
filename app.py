import requests
import time

# Replace with your actual API endpoint
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
        
        # Wait for 5 minutes before sending the next request
        time.sleep(30)

if __name__ == "__main__":
    keep_api_alive()
