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
client = commands.Bot(command_prefix='-r ', help_command=None)


#Posts in terminal that bot is running
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#Posts a random post when given a subreddit syntax '-r random_post subredditname'
@client.command(brief= "<subreddit> Returns a random post from a certain subreddit")
async def random_post(ctx, query="all"):
    try:
        list = []
        subreddit= await reddit.subreddit(query)
        async for submission in subreddit.hot(limit = 10):
            list.append(submission)


        random_sub = random.choice(list)
        em = discord.Embed(title = random_sub.title[:256], 
                            url = reddit.config.reddit_url + random_sub.permalink, 
                            )
        em.add_field(name = "Author: ",  value = random_sub.author)
        em.add_field(name = "Number of upvotes: ", value = random_sub.score)
        em.add_field(name = "Subreddit: ", value = random_sub.subreddit)

        if(random_sub.is_self):
            em.add_field(name = "Description:", value = random_sub.selftext[0:500], inline= False)
        if (random_sub.url[-4:] == '.jpg' or random_sub.url[-4:] == '.png'):
            em.set_image(url = random_sub.url)
        else:
            try:
                em.set_image(url = random_sub.preview['images'][0]['resolutions'][0]['url'])
            except:
                pass

        await ctx.send(embed = em)
    
    except:
        em = discord.Embed(title = "Issue")
        em.add_field(name=" The " + '"'+ query +'"', value='Subreddit was not found', inline= False )
        await ctx.send(embed = em)



@client.command(brief= "<keyword> Returns the top subreddits with the phrase")
async def search_subreddit(ctx, query):
     #subreddits = await reddit.subreddits(query)
    list = []
    async for subreddit in reddit.subreddits.search(query, limit=10):
        list.append(subreddit)

    if not list:
        em = discord.Embed(title = "Issue")
        em.add_field(name=query, value=' was not found in any Subreddits', inline= False )
        await ctx.send(embed = em)
    else: 
        for i in range(len(list)):
            em = discord.Embed(title = list[i].display_name[0:256], url = "https://www.reddit.com/r/"+list[i].display_name+"/")
            em.add_field(name = "Subreddit: ", value = list[i].display_name)
            em.add_field(name = "Subscribers: ", value = list[i].subscribers)
            if(list[i].public_description != ""):
                em.add_field(name = "Description:", value = list[i].public_description[0:500], inline= False)

            await ctx.send(embed = em)
        

@client.command(brief= "<keyword> Return top posts containing a keyword, to return a specific number of posts, use: 'search_post <keyword> <subreddit> (use all for all of reddit) <number of posts>")
async def search_post(ctx, query, subredditname = "all", number="10"):
    num=int(number)
    list_of_rposts = []
    if(subredditname.isnumeric()):
        try:
                num=int(subredditname)
                if(num<=30 and num>=1):
                    subredditname="all"
                    subreddit = await reddit.subreddit(subredditname)
                    async for submission in subreddit.search(query, limit = num):
                        list_of_rposts.append(submission)
                    for i in range(0,num):
                        em = discord.Embed(title = list_of_rposts[i].title[0:256], 
                                url = reddit.config.reddit_url + list_of_rposts[i].permalink, 
                            )
                        em.add_field(name = "Author: ",  value = list_of_rposts[i].author)
                        em.add_field(name = "Number of upvotes: ", value = list_of_rposts[i].score)
                        em.add_field(name = "Subreddit: ", value = list_of_rposts[i].subreddit)

                        if(list_of_rposts[i].is_self):
                            em.add_field(name = "Description:", value = list_of_rposts[i].selftext[0:500], inline= False)
                        if (list_of_rposts[i].url[-4:] == '.jpg' or list_of_rposts[i].url[-4:] ==  '.png'):
                            em.set_image(url = list_of_rposts[i].url)
                        else:
                            try:
                                em.set_image(url = list_of_rposts[i].preview['images'][0]['resolutions'][0]['url'])
                            except:
                                pass


                        await ctx.send(embed = em)
                    return
                elif(num<=0):
                    em = discord.Embed(title = "Issue")
                    em.add_field(name=num , value='is too small, minimum posts is 1', inline= False )
                    await ctx.send(embed = em)
                    return
                else:
                    em = discord.Embed(title = "Issue")
                    em.add_field(name=num , value='is too large, maximum posts is 30', inline= False )
                    await ctx.send(embed = em)
                    return

        except: 
            em = discord.Embed(title = "Issue")
            em.add_field(name= '"'+ query +'"', value='was not found on Reddit', inline= False )
            await ctx.send(embed = em)
            return
    else:
        if(num<=30 and num >=1):
            try:
                subreddit = await reddit.subreddit(subredditname)
                try:
                    async for submission in subreddit.search(query, limit = num):
                        list_of_rposts.append(submission)

                except:
                    em = discord.Embed(title = "Issue")
                    em.add_field(name=" The " + '"'+ subredditname +'"', value='Subreddit was not found', inline= False )
                    await ctx.send(embed = em)
                    return

                for i in range(0,num):
                    em = discord.Embed(title = list_of_rposts[i].title[0:256], 
                            url = reddit.config.reddit_url + list_of_rposts[i].permalink, 
                            )
                    em.add_field(name = "Author: ",  value = list_of_rposts[i].author)
                    em.add_field(name = "Number of upvotes: ", value = list_of_rposts[i].score)
                    em.add_field(name = "Subreddit: ", value = list_of_rposts[i].subreddit)

                    if(list_of_rposts[i].is_self):
                        em.add_field(name = "Description:", value = list_of_rposts[i].selftext[0:500], inline= False)
                    if (list_of_rposts[i].url[-4:] == '.jpg' or list_of_rposts[i].url[-4:] ==  '.png'):
                        em.set_image(url = list_of_rposts[i].url)
                    else:
                        try:
                            em.set_image(url = list_of_rposts[i].preview['images'][0]['resolutions'][0]['url'])
                        except:
                            pass


                    await ctx.send(embed = em)


            except:
                em = discord.Embed(title = "Issue")
                em.add_field(name= '"'+ query +'"', value='was not found in the Subreddit', inline= False )
                await ctx.send(embed = em)
                return
        elif(num<=0):
                    em = discord.Embed(title = "Issue")
                    em.add_field(name=num , value='is too small, minimum posts is 1', inline= False )
                    await ctx.send(embed = em)
                    return
        else:
                em = discord.Embed(title = "Issue")
                em.add_field(name=num , value='is too large, maximum posts is 30', inline= False )
                await ctx.send(embed = em)
                return




         
@client.command(brief = "Return a random meme")
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
    if (random_sub.url[-4:] == '.jpg' or random_sub.url[-4:] == '.png'):
            em.set_image(url = random_sub.url)
    else:
        try:
            em.set_image(url = random_sub.preview['images'][0]['resolutions'][0]['url'])
        except:
            pass
    await ctx.send(embed = em)

@client.command(brief= "Return top 10 posts from all of Reddit")
async def top(ctx):
    list = []
    subreddit= await reddit.subreddit("all")
    async for submission in subreddit.top( time_filter= 'day', limit = 10):
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
        if (list[i].url[-4:] == '.jpg' or list[i].url[-4:] == '.png'):
            em.set_image(url = list[i].url)
        else:
            try:
                em.set_image(url = list[i].preview['images'][0]['resolutions'][0]['url'])
            except:
                pass

        await ctx.send(embed = em)

@client.command(brief= "Post the content of a reddit post given the url")
async def print_post(ctx, url):
    specific_post = await reddit.submission(url=url)

    em = discord.Embed(title = specific_post.title[:256], 
                        url = reddit.config.reddit_url + specific_post.permalink, 
                        )
    em.add_field(name = "Author: ",  value = specific_post.author)
    em.add_field(name = "Number of upvotes: ", value = specific_post.score)
    em.add_field(name = "Subreddit: ", value = specific_post.subreddit)

    
    if(specific_post.is_self):
        em.add_field(name = "Description:", value = specific_post.selftext[0:500], inline= False)
    if (specific_post.url[-4:] == '.jpg' or specific_post.url[-4:] == '.png'):
        em.set_image(url = specific_post.url)
    else:
        try:
            em.set_image(url = specific_post.preview['images'][0]['resolutions'][0]['url'])
        except:
            pass

    await ctx.send(embed = em)


@client.group()
async def help (ctx):
    embed = discord.Embed(title = "Help")
    embed.add_field(name='top', value='Returns the top ten posts of reddit of the day', inline= False )
    embed.add_field(name='meme', value='Returns a meme', inline= False )
    embed.add_field(name='search_post <keyword> <subreddit (optional)> <number (optional)>', value='<keyword> Return top posts containing a keyword, to return a specific number of posts, use: \n "search_post <keyword> <number of posts>"', inline= False )
    embed.add_field(name='search_subreddit <keyword>', value='Returns the top ten subreddits relating to the keyword', inline= False )
    embed.add_field(name='random_post <subreddit>', value='Returns a random post from a subreddit', inline= False )
    embed.add_field(name='print_post <url>', value='Post the content of a reddit post given the url', inline= False )


    await ctx.send(embed= embed)
client.run(token)
