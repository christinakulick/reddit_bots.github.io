# Reddit Bot "bottina123"

## About my bot

_which politician your bot is supporting or opposing_

**My bot opposes the politician and former president Donald Trump**

_Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it_

_output of running the bot_counter.py file on your bot_

```
bot_counter.py
```

## tasks completed:

<ol>
    <li>Each task in bot.py is worth 3 points. **+18**</li>
    <li> The github repo is worth **+2** points </li>
</ol>

### points completed so far: 20

## Extra task completed:

<ol>
    <li>Getting at least 100 valid comments posted. **+2**</li>
    <li>Getting at least 500 valid comments posted. **+2**</li>
    <li>Getting at least 1000 valid comments posted. **+2**</li>
    <li>Make your bot create new submission posts instead of just new comments. You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub. I recommend creating a separate python file for creating submissions and creating comments.For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts. Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count **+2** </li>
    <li>Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible. You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.**+2** </li>
    <li>Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a candidate you do not like). I recommend creating a separate python file for performing the upvotes, and you must be able to upvote comments contained within any submission in the class subreddit. You may earn an additional two points if you use the TextBlob sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate. If the comment/submission has positive sentiment, then upvote it; if the comment/submission has a negative sentiment, then downvote it. **+4**</li>

</ol>

## Total score: 20 + 14 = 34/30 points

<p>I did not complete extra tasks:</p>
<ol>
    <li>Create an "army" of 5 bots that are all posting similar comments. This will require creating 5 different reddit accounts. You can use the same code for each bot (but different praw.ini files with the corresponding login credentials). The challenge is keeping all 5 of these bots running simultaneously. Each bot needs to post at least 500 valid comments to get this extra credit.</li>
    <li>You earn 5 points of extra credit for each of the following tasks you complete. Use a more sophisticated algorithm for generating the text of your comments. There are good python interfaces to the GPT-2 text generation algorithm, like gpt-2-simple, but they can be a bit finicky to get working well. The Markovify library provides an easier to use algorithm that's better than the MadLibs algorithm from lab, but not as good as GPT-2. If you're interested in trying for this extra credit, I'd be happy to discuss how to do this in office hours. </li)>
</ol>
