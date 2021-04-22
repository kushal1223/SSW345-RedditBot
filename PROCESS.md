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

4/21/2021- Today we met to discuss the progress of tasks we delagated a few days ago. Spencer was able to succesfully make the bot respond to the help, top, and meme commands. Christian was able to successfully return reddit posts based on search. Kushal was able to successfully return subreddits based on search. Each group member created their own branch to work on these tasks. Furthermore, each group member created their own pull request to be reviewed by the other groupmates. We will take a look at each other's commits and comment on anything we feel could be added or done better. We plan on fixing these issues by the next meeting so that we can all merge these functions to our main branch.

