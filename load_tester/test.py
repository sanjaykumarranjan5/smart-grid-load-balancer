
import requests
import time

for i in range(23):
    response = requests.post("http://localhost:6000/request_charge")
    print(f"Request {i+1}: {response.json()}")
    time.sleep(0.2)
