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
@client.command(brief= "    Return a random post from a specified subreddit")
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

async def search_post(ctx, query, subredditname = "all"):

    list_of_rposts = []
    subreddit = await reddit.subreddit(subredditname)
    async for submission in subreddit.search(query, limit = 10):
        list_of_rposts.append(submission)

    

    for i in range(0,10):
        em = discord.Embed(title = list_of_rposts[i].title[0:256], 
                            url = reddit.config.reddit_url + list_of_rposts[i].permalink, 
                            )
        em.add_field(name = "Author: ",  value = list_of_rposts[i].author)
        em.add_field(name = "Number of upvotes: ", value = list_of_rposts[i].score)
        em.add_field(name = "Subreddit: ", value = list_of_rposts[i].subreddit)

        if(list_of_rposts[i].is_self):
            em.add_field(name = "Description:", value = list_of_rposts[i].selftext[0:500], inline= False)
        if (list_of_rposts[i].url[-4:] == '.jpg'):
            em.set_image(url = list_of_rposts[i].url)


        await ctx.send(embed = em)
         
@client.command(brief = "    Return a random meme")
async def meme(ctx):
    list = []
    subreddit= await reddit.subreddit('meme')
    async for submission in subreddit.hot(limit = 100):
        list.append(submission)


    random_sub = random.choice(list)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name[0:256], 
                            url = reddit.config.reddit_url + random_sub.permalink, 
                            )
    em.add_field(name = "Author: ",  value = random_sub.author)
    em.add_field(name = "Number of upvotes: ", value = random_sub.score)
    em.add_field(name = "Subreddit: ", value = random_sub.subreddit)

    if(random_sub.is_self):
            em.add_field(name = "Description:", value = random_sub.selftext[0:500], inline= False)
    if (random_sub.url[-4:] == '.jpg'):
            em.set_image(url = random_sub.url)
    await ctx.send(embed = em)

@client.command(brief= "    Return top 10 posts from all of Reddit")
async def top(ctx):
    list = []
    subreddit= await reddit.subreddit("all")
    async for submission in subreddit.top( time_filter= 'day', limit = 11):
        list.append(submission)
    for i in range(0,10):

        em = discord.Embed(title = list[i].title[:256], 
                            url = reddit.config.reddit_url + list[i].permalink, 
                            )
        em.add_field(name = "Author: ",  value = list[i].author)
        em.add_field(name = "Number of upvotes: ", value = list[i].score)
        em.add_field(name = "Subreddit: ", value = list[i].subreddit)

        if(list[i].is_self):
            em.add_field(name = "Description:", value = list[i].selftext[0:500], inline= False)
        if (list[i].url[-4:] == '.jpg'):
            em.set_image(url = list[i].url)

        await ctx.send(embed = em)






client.run(token)
