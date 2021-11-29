import praw
import random
import datetime
import time
from praw.reddit import Subreddit
from textblob import TextBlob

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[TRUMP] [REALLY] needs to stop tweeting. His [TWEETS] are [CRAZY] and [VERY] self-centered.",
    "[LOOKS] as though Trump's wall did not [WORK]. I [HOPE] Trump's [PEOPLE] are [HAPPY] with their weird apparel now.",
    "Aside from Trump's [POLICIES] when he [SPOKE] I was always [WORRIED]. His [WORDS] never came across [ELOQUENTLY].",
    "Trump's [COMMENTS] about women were [HORRIBLE]! As [PRESIDENT] he should have been more [RESPECTFUL] or kept [QUIET].",
    "Trump was even [RUDE] to [PENCE]. He called him [BAD] names and did not appear to [CARE] about him in times of [NEGATIVE] media coverage about his presidency.",
    "Trump will never [LEAVE] the news. He [LOVES] to be the [STAR] too much. He should [RETIRE] soon and learn to [SUPPORT] the new administrations."
]

replacements = {
    'TRUMP' : ['Trump', 'Former President', 'Donald', 'Donald Trump', 'Former President Trump'],
    'REALLY' : ['really', 'absolutely', 'immediately', 'actually','honestly'],
    'TWEETS' : ['tweets', 'posts', 'comments', 'social media sharings', 'messages'],
    'CRAZY' : ['crazy', 'insane', 'riduculous', 'outragous', 'absurd'],
    'VERY' : ['very', 'deeply', 'particularly', 'extremely', 'excessively'],
    'LOOKS' : ['Looks', 'Appears', 'Seems','Comes across', 'Presents'],
    'WORK' : ['work', 'get built', 'succeed', 'get finished', 'every appear'],
    'HOPE' : ['hope', 'pray'],
    'PEOPLE' : ['people', 'followers', 'citizens', 'constituents', 'voters'],
    'HAPPY' : ['happy', 'pleased', 'content', 'satisfied', 'delighted'],
    'POLICIES' : ['policies', 'beliefs', 'laws', 'poltical desires', 'poltical strategies'],
    'SPOKE' : ['spoke', 'talked', 'gave presentations', 'addressed a large crowd', 'made public announcments'],
    'WORRIED' : ['worried', 'concerned', 'anxious', 'distraught', 'nervous'],
    'WORDS' : ['words', 'speech', 'diction'],
    'ELOQUENTLY' : ['elequently', 'smoothly', 'clearly', 'very articulate', 'well-expressed'],
    'COMMENTS' : ['comments', 'statements', 'remarks', 'opinions', 'judgements'],
    'HORRIBLE' : ['horrible', 'gross', 'not pleasent', 'disgusting', 'distasteful'],
    'PRESIDENT' : ['President', 'a leader', 'Head of State', 'President of the U.S', 'The United States President'],
    'RESPECTFUL' : ['respectful', 'humble', 'kind', 'polite', 'civil'],
    'QUIET' : ['quiet', 'silent', 'private', 'secret', 'confidential'],
    'RUDE' : ['rude', 'inconsiderate', 'impolite', 'disrespectful', 'uncivil'],
    'PENCE' : ['Pence', 'Mike Pence', 'the Vice President', 'Vice President Mike Pence', 'VP Pence'],
    'BAD' : ['bad', 'awful', 'mean', 'horrendous', 'nasty'],
    'CARE' : ['care', 'be concerned'],
    'NEGATIVE' : ['negative', 'poor', 'bad', 'bleak', 'substandard'],
    'LEAVE' : ['leave', 'stop appearing in', 'stop being in'],
    'LOVES' : ['loves', 'adores', 'wants', 'enjoys', 'likes'],
    'STAR' : ['star', 'star of the show', 'in the spotlight', 'front and center','the man getting lots of publicity'],
    'RETIRE' : ['retire', 'calm down', 'stop being controversial', 'quiet down'],
    'SUPPORT' : ['support', 'back', 'trust', 'care about', 'approve'],
}

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    s = random.choice(madlibs)

    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return s

#for i in range(100):
    #submission.reply(generate_comment())
   # time.sleep(300)

#for comment in submission.comments.list():
    #for i in range(10):
        #comment.reply(generate_comment())
        #time.sleep(300)

# FIXME done:
# connect to reddit 
reddit = praw.Reddit("bot", user_agent="cs40")

# FIXME done:
# select a "home" submission in the /r/BotTown subreddit to post to
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = submission.comments.list()
 
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    
    not_my_comments = []
    for comment in all_comments:
        #print('comment.author=', comment.author)
        #print('type(comment.author)=', type(comment.author))
        if str(comment.author) != 'bottina123':
            not_my_comments.append(comment)


# Extra Credit 7: upvote submission (in my case downvote since against politician) if mentioned
# an additional two points if you use the TextBlob sentiment analysis library
# ran this on a different file
    '''
    word1 = 'trump'
    word2 = 'biden'
    for comment in not_my_comments:
        if word1.lower() in comment.body.lower():
            comment.downvote()
        elif word2.lower() in comment.body.lower():
            comment.upvote()
    
    for comment in not_my_comments:
        if word1.lower() in comment.body.lower():
            if TextBlob(comment.body).sentiment.polarity > 0:
                comment.downvote()
            elif TextBlob(comment.body).sentiment.polarity < 0:
                comment.upvote()

    subreddit = reddit.subreddit("BotTown2")
    word1 = 'trump'
    word2 = 'biden'
    for sub in subreddit.new(limit=None):
        if word1.lower() in sub.title.lower():
            sub.downvote()
        elif word2.lower() in sub.title.lower():
            sub.upvote()

    for sub in subreddit.new(limit=None):
        if word1.lower() in sub.title.lower():
            if TextBlob(sub.title).sentiment.polarity > 0:
                sub.downvote()
            elif TextBlob(sub.title).sentiment.polarity < 0:
                sub.upvote()
    '''
    
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)


    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment() 
        submission.reply(text)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        
        comments_without_replies = []
        for comment in not_my_comments:
            status = False
            for reply in comment.replies:
                    if reply.author == 'bottina123':
                        status = True
            if status == False:
                comments_without_replies.append(comment)


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        
        
        # ----------------------------------------------------------------------------------------------
        # Extra credit 6: reply to highly upvoted comments first
        #for comment in comments_without_replies:
            #try:
                #comment.reply(generate_comment())
                
            #except (praw.exceptions.APIExceptions, IndexError):
                #print('invalid input')
                #pass
        
        # original code to comment randomly: 

        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except (praw.exceptions.APIExceptions, IndexError):
            print('invalid input')
            pass
    

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    hottest_submissions = []
    subreddit = reddit.subreddit("BotTown2")
    for submission in subreddit.hot(limit=5):
        hottest_submissions.append(submission)
    submission = random.choice(hottest_submissions)
    print('next submission title=', submission.title)
    

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(20)



