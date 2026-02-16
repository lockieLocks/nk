import requests

def check_discord_token(token, txt_list):
    url = "https://discord.com/api/v9/users/@me"
    headers = { 
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return "Valid Token"
    else:
        return "Invalid Token"