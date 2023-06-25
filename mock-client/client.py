import sys
import time
import requests
import random


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"{sys.argv[0]} name IP port", file=sys.stderr)
        exit(-1)

    reporter = sys.argv[1]
    url = sys.argv[2]
    port = sys.argv[3]

    while True:
        post_data = {
            "reporter": reporter,
            "temp": 22 + random.random(),
            "humidity": 51 + random.random() * 3,
            "heatIndex": 24 + random.random() * 2,
        }
        try:
            requests.post(f"http://{url}:{port}/data", json=post_data)
        except:
            print(f"POST on http://{url}:{port}/data failed.", file=sys.stderr)
            exit(0)
        time.sleep(2)
