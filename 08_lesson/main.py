import requests
from config import API_KEY, BASE_URL, TIMEOUT, DEBUG


def get_user_data(user_id: int):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    url = f"{BASE_URL}users/{user_id}"

    if DEBUG:
        print(f"[DEBUG] Making request to {url}")

    response = requests.get(url, headers=headers, timeout=TIMEOUT)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    user_info = get_user_data(42)
    print(user_info)
