import tweepy
from tweepy import OAuthHandler
from time import sleep
from credentials import *

#access and authorize our twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
'''for tweet in tweepy.Cursor(api.search,
							q='#ocean',
							since='2016-11-25',
							until='2016-11-27',
							geocode='1.3552217, 103.8231561,100km',
							lang='fr').items():
'''


# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search, q='#RealisticTattoo').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')
        
        #favorite the tweet
        tweet.favorite()
        print('Favorite the tweet')
        
        #Tweepy error handling is not accounting for following users  
        #that have already been followed, so we can introduce an if statement
        if not tweet.user.following:
            #follow the user who tweeted
            tweet.user.follow()
            print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
