
import praw
import pdb
import re
import os

#selects user account. password is in praw.ini file
reddit = praw.Reddit('9kbabyyyyyyyyyyyyy')

#subreddits to post to
bitcoinsub = reddit.subreddit("bitcoin")
cryptosub = reddit.subreddit("cryptoCurrency")

