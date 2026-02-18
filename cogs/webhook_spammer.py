import aiohttp
import asyncio

async def _webhook_spammer(webhook: str, amount: int, context: str):
    json = {
        "content": context,
    }
    try:
        async with aiohttp.ClientSession() as sack:
            for i in range(amount):
                s = await sack.post(webhook, json=json)
                status = s.status
                if status == 204:
                    print(f"Request POST Sent | Amount: {i+1} | Status Code: {status}")
                else:
                    print(f"Waiting 10 seconds... Status: {status}")
                    await asyncio.sleep(10)
            return f"Spammed {amount} Messages"
    except Exception as e:
        return f"Error >> {e}"

def webhook_spammer(webhook, amount, context):
    return asyncio.run(_webhook_spammer(webhook, amount, context))