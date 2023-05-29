import os
import time
import requests
import random


if __name__ == '__main__':
    SERVER_URL=os.getenv('SERVER_URL', '')
    if not SERVER_URL:
        raise Exception('SERVER_URL not set')

    while True:
        post_data = {
            "temp": 22 + random.random(),
            "humidity": 51 + random.random() * 3,
            "heatIndex": 24 + random.random() * 2
        }
        requests.post(SERVER_URL + "/data", json=post_data)
        time.sleep(2)
