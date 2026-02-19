import requests
from requests.exceptions import RequestException

def delete(webhook: str):
    try:
        r = requests.delete(webhook)
        status = r.status_code
        r.raise_for_status()
        return f"Request DELETE Sent... | Status Code: {status}"
    except RequestException as re:
        return f"Requests Error: {re}"
    except Exception as e:
        return f"Error: {e}"