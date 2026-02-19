import requests
from requests.exceptions import RequestException

def changer(webhook: str, name: str):
    try:
        json = {
            "name": f"{name}",
            "content": " "
        }
        r = requests.patch(webhook, json=json)
        r.raise_for_status()
        status = r.status_code
        return f"Request PATCH Sent... | Name: {name} | Status Code: {status}"
    except RequestException as re:
        return f"Requests ERROR: {re}"
    except Exception as e:
        return f"Error: {e}"