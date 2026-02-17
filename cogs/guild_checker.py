import requests

def get_info(code):
    url = f"https://discord.com/api/v10/invites/vc?with_counts=true"
    r = requests.get(url)
    data = r.json()
    guild_data = data['guild']
    print(f"{guild_data}")

code = "hi"
get_info(code)