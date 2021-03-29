# SSW 345 Design Milestone

Kushal Patel, Spencer Drucker, Christian Kubelle

I pledge my honor to have abided by the Stevens Honor System - KP, SD, CK


<h1>Problem Statement:</h1>
  
  Considering the scope of the internet, a lot of sites offer information to a user. One website that is considered to be a hub for almost any type of information is Reddit.
  Reddit is used by millions of people daily, just like the telecommunication platform Discord. This platform allows users to communicate with friends via text and voice chat.
  Currently, there is no method to share large amounts of information from Reddit on Discord quickly and efficiently. Since Discord is one of the biggest communication platforms,
  there should be a way to share information from one of the largest information platforms in a fast and concise fashion.

<h1>Bot Description:</h1>
  
  Reddit Bot is a bot that searches for information on Reddit.com based on user search terms and will post the information it collected for the user on Discord in the form of text. There is a lot of information the bot
will be able to gather from Reddit such as the URL of the post, the content within the post, the user who created the post, etc. The user will specify what type of information
they want by including keywords when it interacts with the bot. For example, the user can specify if they want to search by posts or search by subreddits. Then, they can 
specify the topic they are interested in, the popularity filter, and the number of posts/subreddits they want the bot to display.


  Reddit bot is a good solution to the problem because it will provide information from Reddit.com without the user needing to leave Discord. The bot is providing analytical results based on specific inquires rather than having a conversation with users. Once Reddit Bot is added to a  Discord Server, it runs in the background and is only "activated" when a user types a message starting with "-r." The bot will provide users with multiple links all at once. This will save users the time from manually searching for topics and viewing one post at a time. Furthermore, users will be able to share 
reddit content more easily with friends.

 Tagline: A simplistic way to search and share content found on Reddit within Discord

<h1>Use Cases:
  
<h2>Use Case 1: Search for posts containing a specific keyword(s)</h2>

<h3>1. Preconditions</h3>

   Reddit Search Bot is installed on Discord

<h3>2. Main Flow</h3>

   User searches for Reddit posts related to specific keywords using Discord[S1]. Bot displays a list of posts related to the keywords including the comments and the usernames
   of the post creators[S2].


<h3>3. Subflows</h3>

   [S1] User types in a keyword on Discord with the search function and with certain filters i.e. number of upvotes, popularity, recency, number of posts, etc.
    
   [S2] Bot will return a list of posts containing the keyword.  

<h3>4. Alternative Flows</h3>

   [E1] No posts related to the keyword found
    
   [E2] Number of posts in the filter exceeds the allowed limit from Bot.


<h2>Use Case 2: Search for Subreddits about a specific keyword</h2>

<h3>1. Preconditions</h3>

   Reddit Search Bot is installed on Discord

<h3>2. Main Flow</h3>

   User searches for a specific keyword on discord with specific filters[S1]. Bot displays a list of Subreddits containing the keyword[S2].


<h3>3. Subflows</h3>

   [S1] User types in a keyword on Discord with the search function and with certain filters i.e. popularity, number of posts, etc.
   
   [S2] Bot will return a list of Subreddit titles with hyperlinks containing the keyword.  
  
<h3>4. Alternative Flows</h3>

   [E1] No Subreddits exist with keyword.
   
   [E2] Number of Subreddits in the filter exceeds the allowed limit from Bot.

  
<h1>Design Sketches:</h1>
 
![Gather Info Bot StoryBoard (4)](https://user-images.githubusercontent.com/62805944/112771149-7b67e580-8ff8-11eb-9e11-106c0d74c2a2.png)

<p align="center">
  <img src="https://user-images.githubusercontent.com/62805944/112772899-66dc1b00-9001-11eb-9d62-1e7fdeafb3b5.JPG" />
</p>


<h1>Architecture Design:</h1>

<p align="center">
  <img src="https://user-images.githubusercontent.com/62805944/112772320-18794d00-8ffe-11eb-92dc-9b55ba928f72.png?" />
</p>


Discord is the front end interface between the user and Reddit Bot. Discord provides and maintains an API Wrapper called “discord.py” that allows for a bot to monitor a discord 
server and adapt to given inputs. This is great for our bot because we won’t have to write code from scratch to implement this functionality and we can spend more time on 
higher-level functionality. For our specific project, we will have Reddit Bot perform actions only when a user starts a message with “-r”. This is to ensure that Reddit Bot is
only activated when intended. After the bot processes the user’s request and gains all necessary information from Reddit, the bot will communicate back to the user by sending
messages through Discord. This interface allows for users to easily share content on Reddit with their friends without having to leave Discord. 



Reddit Bot will process requests by continually running on an Ubuntu server hosted by a cloud computing company such as AWS. Since the uptime and responsiveness of the bot is 
of most importance, using a cloud computing platform is the best course of action due to their reliability. GET requests will be sent from the Ubuntu server using Python 
scripts. These requests will then be sent to Reddit’s servers. Reddit will then return data based on the GET request and the data will then be processed using Python. The 
Ubuntu server will be in constant communication with Discord’s servers as well as Reddit’s servers which will connect all individual components together. 


The team is using Reddit’s API Wrapper called PRAW to obtain relevant information on Reddit. This approach is effective because the bot will be able to retrieve the exact 
information it needs without having to do complex web scraping. The data returned from Reddit’s servers will be in the form of strings or arrays containing strings. This data
will then be processed using Python. Some examples of the types of data that the Reddit servers will return to Reddit Bot are urls of certain reddit posts, comments related to
specific reddit posts, names of popular subreddits, etc.  


Python will be used to process the data since it is effective for string manipulation. All of the information gathered from Reddit will be processed by Python scripts. The 
Python scripts will be running on the Ubuntu Server. Ultimately, Reddit Bot will return information to the user in the form of text or strings and therefore the formatting of 
the response is crucial. The team intends to implement functionality within Reddit Bot to allow the content of a Reddit post to be posted within a Discord Server.
