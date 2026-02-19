import requests
from requests.exceptions import RequestException
import base64

def changer(webhook, file):
    try:
        with open(file, "rb") as f:
            imgur = f.read()
        avatar_enc = base64.b64encode(imgur).decode("utf-8")
        json = {
            "avatar": f"data:image/png;base64,{avatar_enc}"
        }
        r = requests.patch(webhook, json=json)
        status = r.status_code
        r.raise_for_status()
        return f"Request POST Sent... | Status: {status}"
    except RequestException as re:
        return f"Request Error: {re}"
    except Exception as e:
        return f"Error: {e}"
