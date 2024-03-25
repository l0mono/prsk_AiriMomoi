import discord
from config import TOKEN
from test import song

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "曲を教えて":
        await message.channel.send(song())

client.run(TOKEN)