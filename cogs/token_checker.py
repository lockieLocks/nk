import requests
import asyncio
import aiohttp
from pathlib import Path

async def _check_discord_token(token: str, txt_list: bool):
    token_path = Path("tokens.txt")
    url = "https://discord.com/api/v9/users/@me"
    if txt_list:
        with open(token_path, "r") as f:
            tokens = f.read().splitlines()
        results = {}
        async with aiohttp.ClientSession() as sack: # Figured aiohttp was more efficent for multiple requests at once.
            for t in tokens:
                headers = { 
                    "Authorization": t
                }
                response = await sack.get(url, headers=headers)
                if response.status == 200:
                    results[t] = "Valid Token"
                else:
                    results[t] = "Invalid Token"
            await sack.close()
            return results
    headers = { 
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return "Valid Token"
    else:
        return "Invalid Token"

def check_discord_token(token: str, txt_list: bool):
    if txt_list:
        return asyncio.run(_check_discord_token(token, txt_list))
    else:
        return asyncio.run(_check_discord_token(token, False))