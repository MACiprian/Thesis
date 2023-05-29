import time
import requests as r
import random

if __name__ == '__main__':
    while True:
        post_data = {
            "temp": 22 + random.random(),
            "humidity": 51 + random.random() * 3,
            "heatIndex": 24 + random.random() * 2
        }
        r.post('http://localhost:8000/data', json=post_data)
        time.sleep(2)
