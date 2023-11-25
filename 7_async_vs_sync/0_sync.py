import requests
import time

def fetch_url(url):
    response = requests.get(url)
    return response.text

def main():
    urls = ["https://httpbin.org/delay/2" for _ in range(5)]  # Mock API that simulates a delay
    start_time = time.time()

    for url in urls:
        print(fetch_url(url))

    end_time = time.time()
    print(f"Time taken (synchronous): {end_time - start_time} seconds")

main()
