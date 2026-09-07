import os
import requests
import time

url = os.environ["TARGET_URL"].strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    start = time.perf_counter()

    response = requests.get(
        url,
        headers=headers,
        timeout=15,
        allow_redirects=True
    )

    elapsed = time.perf_counter() - start

    print("=" * 60)
    print(f"Requested URL : {url}")
    print(f"Final URL     : {response.url}")
    print(f"Status Code   : {response.status_code}")
    print(f"Response Time : {elapsed:.3f} seconds")

    print("\n--- Response Headers ---")

    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\n--- Cookies ---")

    if response.cookies:
        for cookie in response.cookies:
            print(f"{cookie.name} = {cookie.value}")
    else:
        print("No cookies found.")

    print("\n--- Redirect History ---")

    if response.history:
        for r in response.history:
            location = r.headers.get("Location", "")
            print(f"{r.status_code}: {r.url} -> {location}")
    else:
        print("No redirects.")

    print("=" * 60)

except requests.exceptions.Timeout:
    print("Request timed out.")
    raise

except requests.exceptions.ConnectionError:
    print("Connection error.")
    raise

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
    raise
