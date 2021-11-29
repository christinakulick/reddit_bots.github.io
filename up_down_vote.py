import praw
from praw.reddit import Subreddit
from textblob import TextBlob
import random
import time

reddit = praw.Reddit('bot', user_agent="cs40")

submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)
submission.comments.replace_more(limit=None)
all_comments = submission.comments.list()

# Extra Credit 7: upvote comment if politician is mentioned 
# my bot will downvote when "trump" is detected and to get more votes will upvote when "biden" is detected
# +4 for using TextBlob sentiment polarity
while True: 
    upvoted = 0
    downvoted = 0
    for comment in all_comments:
        words = TextBlob(comment.body.lower())
        polarity = words.sentiment.polarity
        if 'trump' in comment.body.lower() and polarity > 0:
            comment.downvote()
            downvoted +=1
        if 'biden' in comment.body.lower() and polarity > 0:
            comment.upvote()
            upvoted += 1
        if 'trump' in comment.body.lower() and polarity < 0:
            comment.upvote()
            upvoted += 1
        if 'biden' in comment.body.lower() and polarity < 0:
            comment.downvote()
            downvoted += 1
        else:
            print('no upvote or downvote')
        
    print('# upvoted =', upvoted)
    print('# downvoted =', downvoted)

    sub_upvote = 0
    sub_downvote = 0
    subreddit = reddit.subreddit("BotTown2")
    for sub in subreddit.new:
        sentence = TextBlob(submission.title.lower())
        polarity = sentence.sentiment.polarity
        if 'trump' in submission.title.lower() and polarity > 0:
            sub.downvote()
            sub_downvote += 1
        if 'biden' in submission.title.lower() and polarity > 0:
            sub.upvote()
            sub_upvote += 1
        if 'trump' in submission.title.lower() and polarity < 0:
            sub.upvote()
            sub_upvote += 1
        if 'biden' in submission.title.lower() and polarity < 0:
            sub.downvote()
            sub_downvote += 1
        else:
            print('no upvote or downvote')

    print('# sub upvoted =', sub_upvote)
    print('# sub downvoted =', sub_downvote)

    hottest_submissions = []
    subreddit = reddit.subreddit("BotTown2")
    for submission in subreddit.hot(limit=5):
        hottest_submissions.append(submission)
    submission = random.choice(hottest_submissions)
    print('next submission title=', submission.title)
  
    time.sleep(20)
