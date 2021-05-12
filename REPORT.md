
# SSW 345 Final Report
### Spencer Drucker, Christian Kubelle, Kushal Patel
 
*I pledge my honor that I have abided by the Stevens Honor System.- SD,CK,KP*

## Problem Solved
Considering the scope of the internet, a lot of sites offer information to a user. One website that is considered to be a hub for almost any type of information is Reddit. Reddit is used by millions of people daily, just like the telecommunication platform Discord. This platform allows users to communicate with friends via text and voice chat. Currently, there is no method to share large amounts of information from Reddit on Discord quickly and efficiently. Since Discord is one of the biggest communication platforms, there should be a way to share information from one of the largest information platforms in a fast and concise fashion. RedditBot allows information on Reddit to be shared among other Discord users without anyone needing to leaving Discord.

## Primary Features

### '-r help'
After installing RedditBot onto the user’s server, the user needs to be able to see the list of commands available to them. To do this, they can simply type “-r help” to see a list of all available commands.

![image](https://user-images.githubusercontent.com/44238558/118015200-05a6a780-b322-11eb-875b-34288060fdd5.png)

*The RedditBot help command in use*



### '-r top'
The top command will return the top ten posts on the home page of Reddit.com. This command will embed links to the original posts within the title of the post and will display the author of the post, the number of upvotes on the post, and the subreddit where the post was originally posted.

![image](https://user-images.githubusercontent.com/44238558/118015583-7221a680-b322-11eb-9f85-882588e30bac.png)
![image](https://user-images.githubusercontent.com/44238558/118015675-8b2a5780-b322-11eb-8f8c-26a9f429024f.png)
![image](https://user-images.githubusercontent.com/44238558/118015761-a1d0ae80-b322-11eb-951f-88c8058672a3.png)
![image](https://user-images.githubusercontent.com/44238558/118015840-b745d880-b322-11eb-8030-dab80b8b8383.png)
![image](https://user-images.githubusercontent.com/44238558/118015877-c2006d80-b322-11eb-9560-862ffe5d8ff7.png)
![image](https://user-images.githubusercontent.com/44238558/118015921-cd539900-b322-11eb-8590-59ece6b29187.png)

*The returns of RedditBot for “-r top” on 5/12/2021 at 12:23pm*

For verification purposes here is a screenshot of the top ten reddit posts from reddit.com directly. This is to show that the bot is extracting the correct information.
![image](https://user-images.githubusercontent.com/44238558/118017119-38519f80-b324-11eb-9458-0402abedff49.png)



### '-r meme'
Typing in “-r meme” will return a meme from the “meme” subreddit along with the author of the post and the number of upvotes.  This command will embed the link to the original poss within the title of the post and will display the author of the post, the number of upvotes on the post, the post’s description, and the subreddit where the post was originally posted.

![image](https://user-images.githubusercontent.com/44238558/118017556-c3329a00-b324-11eb-9486-9f474b1b588b.png)

*This is the “-r meme” function being used*

### '-r search_post'
The purpose of this function is to scrape reddit and return posts related to user search. If the user types in “-r search_post <keyword>”, it will return the top ten posts on all of Reddit.com containing the keyword. This command will embed links to the original posts within the title of the post and will display the author of the post, the number of upvotes on the post, the post’s description, and the subreddit where the post was originally posted.

![image](https://user-images.githubusercontent.com/44238558/118018126-6683af00-b325-11eb-83af-0ec3651db832.png)
![image](https://user-images.githubusercontent.com/44238558/118018185-79967f00-b325-11eb-8931-760d1af3298c.png)
![image](https://user-images.githubusercontent.com/44238558/118018216-84511400-b325-11eb-89d8-20ef18de1fed.png)
![image](https://user-images.githubusercontent.com/44238558/118018331-a34fa600-b325-11eb-9514-1c94e6d70022.png)
![image](https://user-images.githubusercontent.com/44238558/118018408-bb272a00-b325-11eb-8ff5-93c5c9998629.png)
![image](https://user-images.githubusercontent.com/44238558/118018434-c5e1bf00-b325-11eb-8dc3-f416e36108e9.png)

*The “-r search_post” function with “happy” as the keyword returning 10 posts*

This function additionally supports a user to type in the number of posts they wish RedditBot to return. If the user were to type the same phrase, “-r search_post keyword number” RedditBot will return the number of posts the user specified. It should be noted that RedditBot will not return any posts greater than 30. We did this purposely to ensure no one is spamming the bot requesting a large amount of posts.

![image](https://user-images.githubusercontent.com/44238558/118019079-92536480-b326-11eb-8385-5e57da6c215f.png)

*The bot returning 2 posts containing the keyword dog*

The final functionality of this command allows for a user to search for posts within a specific subreddit. Reddit categorizes different posts within subreddits. Subreddits can be thought of generally as different topics or categories people can post within. For example, there is a 'dog' subreddit and a 'stocks' subreddit with each subredding containing posts about their respective name. 

A user may wish to lookup information about DOGE, a popular cryptocurrency, within the subreddit named "wallstreetbets" because of users within the subreddit talking about the coin greatly. To do so, the user would do the following:

![image](https://user-images.githubusercontent.com/44238558/118019881-7b614200-b327-11eb-8a2e-8d216e71cc72.png)


### '-r search_subreddit'
If a user wishes to find the top ten subreddits related to a certain keyword, they can do so with the '-r search_subreddit' command. The function will return the top ten subreddits resulting from the keyword given by the user on Discord along with a link to the subreddit, the title of the subreddit, the number of subscribers that the subreddit has, and a description, if any. This is accomplished when the user types in “-r search_subreddit keyword”. 

Lets imagine a user wanted to find the most popular subreddits related to basketball. They could do so by doing the following:

![image](https://user-images.githubusercontent.com/44238558/118021074-d7789600-b328-11eb-9ea6-e458ef4827d4.png)
![image](https://user-images.githubusercontent.com/44238558/118021260-0989f800-b329-11eb-8083-5bcf26774cdf.png)
![image](https://user-images.githubusercontent.com/44238558/118021154-ea8b6600-b328-11eb-9364-51a60bac0a3d.png)

*The “-r search_subreddit” function with “basketball” as the keyword returning 10 subreddits*


