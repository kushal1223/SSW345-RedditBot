# SSW 345 Design Milestone

Kushal Patel, Spencer Drucker, Christian Kubelle

I pledge my honor to have abided by the Stevens Honor System - KP, SD, CK


<h1>Problem Statement:
  
  <h3>Considering the scope of the internet, a lot of sites offer information to a user. One website that is considered to be a hub for almost any type of information is Reddit.
  Reddit is used by millions of people daily, just like the telecommunication platform Discord. This platform allows users to communicate with friends via text and voice chat.
  Currently, there is no method to share large amounts of information from Reddit on Discord quickly and efficiently. Since Discord is one of the biggest communication platforms,
  there should be a way to share information from one of the largest information platforms in a fast and concise fashion.

<h1>Bot Description:
  
  <h3>The bot will gather information from Reddit.com and will post the information it collected for the user on Discord in the form of text. There is a lot of information the bot
will be able to gather from Reddit such as the URL of the post, the content within the post, the user who created the post, etc. The user will specify what type of information
they want by including keywords when it interacts with the bot. For example, the user can specify if they want to search by posts or search by subreddits. Then, they can 
specify the topic they are interested in, the popularity filter, and the number of posts/subreddits they want the bot to display.


<h3>The bot is a good solution to the problem because it will provide information from Reddit.com without the user needing to leave Discord. The Reddit Bot will provide users 
with multiple links all at once. This will save users the time from manually searching for topics and viewing one post at a time. Furthermore, users will be able to share 
reddit content more easily with friends.

  
<h1>Use Cases:
  
<h2>Use Case 1: Search for posts containing a specific keyword(s)<h2>

1. Preconditions

   Reddit Search Bot is installed on Discord

2. Main Flow

   User searches for Reddit posts related to specific keywords using Discord[S1]. Bot displays a list of posts related to the keywords including the comments and the usernames
   of the post creators[S2].


3. Subflows

    [S1] User types in a keyword on Discord with the search function and with certain filters i.e. number of upvotes, popularity, recency, number of posts, etc.
    
    [S2] Bot will return a list of posts containing the keyword.  

4. Alternative Flows

    [E1] No posts related to the keyword found
    
    [E2] Number of posts in the filter exceeds the allowed limit from Bot.



<h2>Use Case 2: Search for Subreddits about a specific keyword<h2>

1. Preconditions

   Reddit Search Bot is installed on Discord

2. Main Flow

   User searches for a specific keyword on discord with specific filters[S1]. Bot displays a list of Subreddits containing the keyword[S2].


3. Subflows

   [S1] User types in a keyword on Discord with the search function and with certain filters i.e. popularity, number of posts, etc.
   
   [S2] Bot will return a list of Subreddit titles with hyperlinks containing the keyword.  
  
4. Alternative Flows

   [E1] No Subreddits exist with keyword.
   
   [E2] Number of Subreddits in the filter exceeds the allowed limit from Bot.

  
<h1>Design Sketches:
 
![Gather Info Bot StoryBoard (4)](https://user-images.githubusercontent.com/62805944/112771149-7b67e580-8ff8-11eb-9e11-106c0d74c2a2.png)

<h1>Architecture Design:
