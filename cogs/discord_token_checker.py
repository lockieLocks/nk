import requests

def check_discord_token(token: str, txt_list: bool):
    url = "https://discord.com/api/v9/users/@me"
    if txt_list:
        with open(token, "r") as f:
            tokens = f.read().splitlines()
        results = {}
        for t in tokens:
            headers = { 
                "Authorization": t
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                results[t] = "Valid Token"
            else:
                results[t] = "Invalid Token"
        return results
    headers = { 
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return "Valid Token"
    else:
        return "Invalid Token"