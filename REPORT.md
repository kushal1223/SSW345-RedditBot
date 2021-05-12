
# SSW 345 Final Report
### Spencer Drucker, Christian Kubelle, Kushal Patel
 
*I pledge my honor that I have abided by the Stevens Honor System.- SD,CK,KP*

## Problem Solved
Considering the scope of the internet, a lot of sites offer information to a user. One website that is considered to be a hub for almost any type of information is Reddit. Reddit is used by millions of people daily, just like the telecommunication platform Discord. This platform allows users to communicate with friends via text and voice chat. Currently, there is no method to share large amounts of information from Reddit on Discord quickly and efficiently. Since Discord is one of the biggest communication platforms, there should be a way to share information from one of the largest information platforms in a fast and concise fashion. RedditBot allows information on Reddit to be shared among other Discord users without anyone needing to leave Discord.

## Primary Features

### '-r help'
After installing RedditBot onto the user’s server, the user needs to be able to see the list of commands available to them. To do this, they can simply type “-r help” to see a list of all available commands.

![image](https://user-images.githubusercontent.com/44238558/118015200-05a6a780-b322-11eb-875b-34288060fdd5.png)

*The RedditBot help command in use*



### '-r top'
 If the user wants to show their friends the top ten posts on all of Reddit for the day without having to copy and paste each link, they can simply use the “-r top” command. The top command will return the top ten posts on the home page of Reddit.com. This command will embed links to the original posts within the title of the post and will display the author of the post, the number of upvotes on the post, and the subreddit where the post was originally posted.

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
If the user would like to make their friend laugh with a random funny meme, typing in “-r meme” will return a meme from the “meme” subreddit along with the author of the post and the number of upvotes. This command will embed the link to the original poss within the title of the post and will display the author of the post, the number of upvotes on the post, the post’s description, and the subreddit where the post was originally posted.

![image](https://user-images.githubusercontent.com/44238558/118017556-c3329a00-b324-11eb-9486-9f474b1b588b.png)

*This is the “-r meme” function being used*

### '-r search_post'
The purpose of this function is to scrape reddit and return posts related to user search. If the user types in “-r search_post <keyword>”, it will return the top ten posts on all of Reddit.com containing the keyword. This is a great way to get updates and information on that keyword without having to look up individual posts. This command will embed links to the original posts within the title of the post and will display the author of the post, the number of upvotes on the post, the post’s description, and the subreddit where the post was originally posted.

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

Optionally, the user can also enter the name of a specific subreddit that they would like to search for the keyword in, along with an optional number of posts as well (if the number is not specified, it will default to 10). Having a specific subreddit to search the keyword in, helps in streamlining the information by gathering it from one specific spot. Reddit categorizes different posts within subreddits. Subreddits can be thought of generally as different topics or categories people can post within. For example, there is a 'dog' subreddit and a 'stocks' subreddit with each subredding containing posts about their respective name. 

A user may wish to lookup information about DOGE, a popular cryptocurrency, within the subreddit named "wallstreetbets" because of users within the subreddit talking about the coin greatly. To do so, the user would do the following:

![image](https://user-images.githubusercontent.com/44238558/118019881-7b614200-b327-11eb-8a2e-8d216e71cc72.png)


### '-r search_subreddit'
If a user wishes to find the top ten subreddits related to a certain keyword, they can do so with the '-r search_subreddit' command. The function will return the top ten subreddits resulting from the keyword given by the user on Discord along with a link to the subreddit, the title of the subreddit, the number of subscribers that the subreddit has, and a description, if any. This is accomplished when the user types in “-r search_subreddit keyword”. 

Lets imagine a user wanted to find the most popular subreddits related to basketball. They could do so by doing the following:

![image](https://user-images.githubusercontent.com/44238558/118021074-d7789600-b328-11eb-9ea6-e458ef4827d4.png)
![image](https://user-images.githubusercontent.com/44238558/118021260-0989f800-b329-11eb-8083-5bcf26774cdf.png)
![image](https://user-images.githubusercontent.com/44238558/118021154-ea8b6600-b328-11eb-9364-51a60bac0a3d.png)

*The “-r search_subreddit” function with “basketball” as the keyword returning 10 subreddits*

### '-r random_post'
This function will return a random post resulting from the subreddit given by the user on Discord along with the author of the post, the number of upvotes, the subreddit that the post is from, and a description, if any. This is accomplished when the user types in “-r random_post subreddit”.

![image](https://user-images.githubusercontent.com/44238558/118021726-8ae18a80-b329-11eb-9380-f7f0cc4df63e.png)

*The “-r random_post” function with “stocks” as the subreddit returning a post*


### '-r print_post'
The last function is the print_post function. This function will return the post resulting from the url given by the user on Discord along with the author of the post, the number of upvotes, the subreddit the post is from, and a description, if any. The url can be obtained from Reddit. This is useful because it allows users on Discord to see the post without having to go to Reddit. This is accomplished when the user types in “-r print_post url”.

Lets imagine that a user had a certain Reddit post they wanted to share among their friends on Discord. It would be timely for each Discord member to have to click the link, open a web browser, and load the webpage just to look at the post. Instead the original Discord user wanting to share the post can use the "-r print_post" command.

![image](https://user-images.githubusercontent.com/44238558/118022077-f3c90280-b329-11eb-87f9-d69c426cccae.png)

### Error Handling
Since there are certain commands that take in keywords or subreddits from the users on Discord, our group also had to account for any errors that may result from certain inputs. For these commands, we did multiple tests within Discord to see how our bot would respond if the provided keyword was unable to be found, or the provided subreddit did not exist. After testing out multiple inputs that could result in errors, we were able to successfully provide users with an error message relating to the improper input that the bot received. Furthermore, to account for users putting into a large number of desired posts, we decided that the maximum number of posts that could be returned is 30. The following images provide some examples of error messages.

![image](https://user-images.githubusercontent.com/44238558/118024189-62a75b00-b32c-11eb-8b9a-1bafdeed1a3c.png)
![image](https://user-images.githubusercontent.com/44238558/118024639-ef521900-b32c-11eb-94a9-39ed8062ebce.png)
![image](https://user-images.githubusercontent.com/44238558/118024282-84a0dd80-b32c-11eb-8f02-de5d8cd53db2.png)
![image](https://user-images.githubusercontent.com/44238558/118024346-94202680-b32c-11eb-84d9-7b34345ef868.png)

## Reflection
Looking back on the project, all groupmates can agree that this was one of the most enjoyable projects we have worked on throughout our college career. The use of Discord’s API along with Reddit’s PRAW were both relatively simple tools to understand and use. We all feel that the development process was seamless the entire time. With the use of the Kanban board on GitHub, we were very easily able to divide tasks and list the subtasks to help guide us throughout the development of each task. Throughout the entire development process, we had a constant stream of communication, constantly meeting to discuss issues, fixes, updates, and anything else that we felt necessary. Also with the use of branching and merging on GitHub, we were able to maximize our independent efficiency, since we did not have to rely on each other to push code. Overall, with the easy-to-use tools, streamlined workflow, and constant communication, this project was a fun and unique experience that we are all extremely proud of.

## Limitations and Future Work
Looking back on the development process and project, our group did not have many limitations. Some small things may include a lack of familiarity with Reddit’s PRAW which might have some advanced features that we did not make use of which could have made our project better. However, the tools that we used were not too hard to understand, so this issue mostly stems from us having to meet deadlines and finish our work at a certain time. The only real limitation was Discord’s embedding of videos. Discord does not allow bots to post videos, so any videos on Reddit.com could not be displayed, so we were forced to change the videos into a picture to display instead.


As far as any future work moving forward, our group feels like our bot would be very useful for Discord users, so we plan to continue to add functionality if we find anything else that can be added. We currently have this bot deployed on an Ubuntu server using AWS and in the future we will keep it deployed.


