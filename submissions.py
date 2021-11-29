from logging import error
import praw
import random
import time
import datetime
from praw import reddit
from praw.reddit import Subreddit

#EC task 4: creating submissions

reddit = praw.Reddit('bot', user_agent="cs40")
reddit.validate_on_submit = True 

submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)
subreddit_other = reddit.subreddit('PoliticalDiscussion')
subreddit_home = reddit.subreddit('BotTown2')

for sub in subreddit_other.top(limit=300):
    try:
        subreddit_home.submit(sub.title, url=sub.url)
    except praw.exceptions.RedditAPIException:
        print('error found')
        time.sleep(20)


  


