import requests as req

def check_webhook(webhook: str):
    resp = req.get(webhook)
    if resp.status_code == 200:
        data = resp.json()
        lines = [f"{k}, {v}" for k, v in data.items()]
        return "\n".join(lines)
    else:
        return "Invalid Webhook"

print(check_webhook("https://discord.com/api/webhooks/1467034301869719653/wXJ1HktxoakSIUFtESjfEvcFVaUtLBlASREK4bAxXn40vCe41si0ImnT3agi1P6OgvUK"))