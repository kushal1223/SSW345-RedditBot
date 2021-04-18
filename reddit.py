#File to test reddit API out 
#For testing purposes only

import asyncpraw
import requests
import pandas as pd
import praw


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
reddit = praw.Reddit(
    client_id = clientid,
    client_secret = secretkey,
    username = username,
    password = pw,
    user_agent = "RedditBot"
)


#Test Code here

#list = reddit.subreddits.search_by_name("stocks")

for submission in reddit.subreddit("all").hot(limit=25):
    print(submission.title)

#for post in list:
#    print(post)
