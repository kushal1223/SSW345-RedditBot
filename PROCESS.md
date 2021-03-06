# Process Milestone


## First Iteration - (Monday Mar 29  Sunday Apr 11)

4/5/2021- Today we created our Progress Board for the project. We created three tasks to start the project: Setup Server, Setting up Reddit API, and Setup Basic Discord Bot. We plan to get the first section of the project done by Sunday, April 11, 2021.

### A Screenshot of our Progress Board
![image](https://user-images.githubusercontent.com/44238558/114332838-fb23a300-9b14-11eb-933d-3d84286808ea.png)


4/8/2021- Today we delegated the tasks that need to be done and talked about how we will approach each task. We tried to fairly partition the work among the three group members by estimating how long each task will take and splitting the work equally. We choose to undergo the tasks that we felt most comfortable with. Christian will be working on setting up the server necessary for the Bot. Kushal will work on the Reddit API. Spencer will work on setting up a Discord bot. We also familiarized ourselves with the Progress Board which we will be using throughout the project. We also delegated complexity points to the tasks on the board. 


4/11/2021 - We discussed our progress for each task that we were working on. Starting with Christian, he was able to setup a Ubuntu server using AWS and run a simple python script to test that the environment was setup properly. He used PuTTy to connect to the server using ssh, and transferred over necessary files using FileZilla. Overall the task was not that challenging however, he had issues connecting to the server initially since he had to create secret and public keys to connect to it. AWS provides free tier servers which is great for a project like this because it allows us to not worry about paying to run the bot. Over the course of this iteration Kushal worked on making a python script that gathers data from Reddit using Reddit's API called PRAW. In order to do this, he had to create a development app within Reddit to submit GET requests. This was initially hard because it was confusing how to gather the private key necessary for the API. Nonetheless, he was able to get the script working correctly. He used Jupyter Notebook to visualize the dataset. We have a screenshot of an example output posted below. Spencer worked on creating the Discord Bot through Discord's platform and was able to successfully get the bot to respond to a message on a Discord server. Overall, we were able to complete the tasks on time and we spent the last portion of the meeting discussing the tasks we will be working on next. In terms of our process reflection we feel that the progress we have made so far is good but we will need to stay consistent within these next couple of weeks. We have setup the initial stuff, which was easy, and we will now be working on more complex issues. As a group, we have really liked working on this project because we had the freedom to create the type of bot we would like and we also see value in the fact that we can use this Bot in the future.

### Our Updated Progress Board
![image](https://user-images.githubusercontent.com/44238558/114334765-48097880-9b19-11eb-9dbf-52908007fbc5.png)

### A Screenshot of our working Reddit API
![redditapi](https://user-images.githubusercontent.com/62805944/114334641-011b8300-9b19-11eb-9c6b-0910d0ae9247.PNG)

### A Screenshot of successful Discord Bot response
![botresponse](https://user-images.githubusercontent.com/62805944/114337665-86a23180-9b1f-11eb-9ed0-bd32654f0710.PNG)

## Second Iteration - (Monday Apr 12  Sunday Apr 25)

4/15/2021 - Today we met to delegate work and discuss what are the next steps we need to take. We worked with setting up the reddit portion of the bot with the discord portion. Meaning that once a user enters information in discord, the bot responds with information coming from reddit.com. We were able to get it so that if a user types a message starting with "-r" Redditbot will respond with information gathered from the soccer subreddit. The next step is to change the bots response based on user input.

4/17/2021- Christian worked on connecting the Reddit API to the Discord files. Spencer worked on making the Discord function asynchronous. Kushal worked on editing Reddit and Discord files.


4/19/2021- Today we delegated tasks to work on within the index.py file. We assigned the following functions: search subreddits, search all of Reddit, return posts based on search. We also made secondary tasks such as filtering by hot or top posts, and the number of searches. 

Spencer: Help command, Top command, Meme command.
Christian: Return Reddit posts based on search.
Kushal: Returning Subreddits .

4/21/2021- Today we met to discuss the progress of tasks we delagated a few days ago. Spencer was able to successfully make the bot respond to the help, top, and meme commands. Christian was able to successfully return reddit posts based on search. Kushal was able to successfully return subreddits based on search. Each group member created their own branch to work on these tasks. Furthermore, each group member created their own pull request to be reviewed by the other groupmates. We will take a look at each other's commits and comment on anything we feel could be added or done better. We plan on fixing these issues by the next meeting so that we can all merge these functions to our main branch. 
### Image of our pull requests
![image](https://user-images.githubusercontent.com/44238558/115638752-f4e5b180-a2e0-11eb-98da-76a5101b2195.png)

We also started adding more descriptive cards to our project board. We are now using issues within our project board which allows us to assign them to each other and use labels to highlight their importance.

### Screenshot of our Project Board currently

![image](https://user-images.githubusercontent.com/44238558/115638885-3fffc480-a2e1-11eb-9e16-09c57d6bb26b.png)

We now have multiple branches based on the work we are delegating. We waited to create multiple branches until our main architecture was created so that when we all merge branches, we should not have to worry too much

### Screenshot of our active branches
![image](https://user-images.githubusercontent.com/44238558/115639218-0f6c5a80-a2e2-11eb-9715-37098db72ca4.png)

4/22/2021- After receiving feedback from each of our group members, we spent some time trying to improve the functions that we created. We fixed most issues for our functions and were able to close our pull requests after successfully merging all of our new code to the main branch. Some things that we need to continue working on include updating the help command, properly displaying a video within a post, and properly displaying the time that subreddits are created. In addition, we plan on implementing a feature to the search_post and search_subreddit command that allows users to input the amount of posts/subreddits they want the bot to return.

### Image of closed pull requests
![closed pull requests](https://user-images.githubusercontent.com/62805944/116011423-ea822b00-a5f2-11eb-9ceb-b7f0c1793dea.PNG)


The following images show the Reddit Bot responding to the commands that we implemented during this iteration:

### -r help
### Returns a post that provides the user with all available commands


![-r help](https://user-images.githubusercontent.com/62805944/116010837-7f832500-a5ef-11eb-82a6-886c8842ea23.PNG)

### -r search post
### Returns top ten posts containing the keyword (can be in a specific subreddit)


![-r search post](https://user-images.githubusercontent.com/62805944/116010846-91fd5e80-a5ef-11eb-9de6-5963cd5d81a8.PNG)

### -r search subreddit
### Returns the top ten subreddits relating to the keyword


![-r search subreddit](https://user-images.githubusercontent.com/62805944/116010850-975aa900-a5ef-11eb-8bd8-4e7f53c071d5.PNG)

### -r meme
### Returns a meme


![-r meme](https://user-images.githubusercontent.com/62805944/116010856-9cb7f380-a5ef-11eb-8122-fd490e95b0b3.PNG)

### -r top
### Returns the top ten posts of reddit of the day


![-r top updated](https://user-images.githubusercontent.com/62805944/116011069-0258af80-a5f1-11eb-9f7e-2375fe146c44.PNG)

### Example of one of our Merge Requests
After making each our own branch, we each submitted a merge request. Similar to the lab we did in class, we assigned each other as reviewers and made comments based on improvements we can make.
![image](https://user-images.githubusercontent.com/44238558/116011747-924c2880-a5f4-11eb-9e88-36ec3fa7687f.png)


### End of Iteration Two
4/25/2021 - Today we met to discuss the end of iteration two and the progress we have made on RedditBot. Overall, we have implemented the main functionality of the bot. We successfully merged all of our branches into main. Going forward, we are going to focus heavily on testing and adding additional functionality/commands to the bot. Our bot is in a working state and we are going to spend the next day or two solely on testing before adding additional commands to the bot. To test the bot we will be assigning each member another person's code to look over and test. We are doing this so we can better understand each other's work and maybe find bugs that the originial developer did not account for. In terms of incomplete tasks we still need to work on our help command and fix the random post command which was not working as intended.

### End of Iteration Two Progress Board
![image](https://user-images.githubusercontent.com/44238558/116011692-397c9000-a5f4-11eb-9c6c-3b22fd7d673b.png)

