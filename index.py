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

        #List of arguments, splits arguments based on spaces, lowercases all letters
        args = message.content.lower().split()

        #Only do something if message starts with '-r'
        if args[0] == '-r':

            #Example of how we can determine which function a user wants
            if args[1] == 'subreddit':
                await message.channel.send(reddit.main(args[2]))
            if args[1] == 'search':
                await message.channel.send(reddit.main(args[2]))


client.run(token)