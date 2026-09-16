import requests


BASE_URL = "https://v2.jokeapi.dev/joke"


def get_random_joke(category: str) -> str:
    url = f"{BASE_URL}/{category}"

    response = requests.get(
        url,
        params={
            "safe-mode": "",
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    if data.get("error"):
        raise Exception(data.get("message", "Failed to fetch joke"))

    if data["type"] == "single":
        return data["joke"]

    return f"{data['setup']}\n\n{data['delivery']}"