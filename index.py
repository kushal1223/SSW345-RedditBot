# bot.py
import os
import reddit
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if '-r' in message.content:
          await message.channel.send(reddit.main("soccer"))


client.run(token)