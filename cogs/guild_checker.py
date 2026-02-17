import requests

def get_info(code):
    url = f"https://discord.com/api/v10/invites/{code}?with_counts=true"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        guild_data = data.get("guild")
        if not guild_data:
            return "No guild info found for that invite."
        return (
            f"Guild ID: {guild_data.get('id')}\n"
            f"Name: {guild_data.get('name')}\n"
            f"Description: {guild_data.get('description')}"
        )
    except requests.RequestException as re:
        return f"Invalid Invite Code | Error: {re}"
    except Exception as e:
        return f"Exception Error: {e}"