# bot.py
import os
import reddit
import discord
from dotenv import load_dotenv
import praw
from discord.ext import commands
import random
import asyncpraw

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#Opening secret files
with open('./secretfiles/pw.txt', 'r') as f:
    pw = f.read()

with open('./secretfiles/secretkey.txt', 'r') as f:
    secretkey = f.read()

with open('./secretfiles/username.txt', 'r') as f:
    username = f.read()

with open('./secretfiles/clientid.txt', 'r') as f:
    clientid = f.read()


#Reddit credentials
reddit = asyncpraw.Reddit(
    client_id = clientid,
    client_secret = secretkey,
    username = username,
    password = pw,
    user_agent = "RedditBot"
)

client = commands.Bot(command_prefix='-r ')


#Posts in terminal that bot is running
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#Posts a random post when given a subreddit syntax '-r random_post subredditname'
@client.command()
async def random_post(ctx, query):
    list = []
    subreddit= await reddit.subreddit(query)
    async for submission in subreddit.hot(limit = 10):
        list.append(submission)

    random_sub = random.choice(list)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)


    await ctx.send(embed = em)

@client.command()
async def search_subreddit(ctx, query):

    #subreddits = await reddit.subreddits(query)
    list = []
    async for subreddit in reddit.subreddits.search(query, limit=10):
        list.append(subreddit)


    for i in range(0,10):
        em = discord.Embed(title = list[i].display_name[0:256], url = "https://www.reddit.com/r/"+list[i].display_name+"/")
        em.add_field(name = "Subreddit: ", value = list[i].display_name)
        em.add_field(name = "Subscribers: ", value = list[i].subscribers)
        if(list[i].public_description != ""):
            em.add_field(name = "Description:", value = list[i].public_description[0:500], inline= False)

        await ctx.send(embed = em)

client.run(token)
