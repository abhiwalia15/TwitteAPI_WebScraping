import re
import tweepy
from tweepy import OAuthHandler
import textblob 

class TwitterClient(object):
	'''generic twitter class for sentimental analysis'''
	
	def __init__(self):
		'''class constructor 
		KEYS AND TOKENS for the TWITTER DEV CONSOLE'''
		
		# Variables that contains the user credentials to access Twitter API 
		ACCESS_TOKEN = '1050006838366810112-vayi2L8Q1vxbPbUOdibmw7CYQhb72g'
		ACCESS_SECRET = 'V4cCohGfJa30T8agz5LgStpNUqDetXbEmWjjSaiC8bpJc'
		CONSUMER_KEY = 'H09lz1MRceBRko8xt86OIlv5i'
		CONSUMER_SECRET = 'MtDWYPzXUxhEXfL5HQcKSSig0ncynEprZfyTJ7hIezHISWSOTa'
		
		#attempt for authentication
		try:
			#create OAUTHHANDLER object
			self.auth = OAuthHandler(cONSUMER_KEY, CONSUMER_SECRET)
			#set access token and secret
			self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
			#create tweepy api object to fetch the tweets from twitter
			self.api = tweepy.API(self.auth)
			
		#else print an error message
		except: 
			print("Error: Authentication Failed")
			
	def clean_tweet(self, tweet):
		''' Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. '''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
		
	def get_tweet_sentiment(self, tweet):
		'''utility function to classify sentiment of passed tweet using textblob's sentiment method'''
		
		#create TEXTBLOB object of passes tweet text
		analysis = textblob(self.clean_tweet(tweet))
		#set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'
			
	def get_tweets(self, query, count = 10): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 
  
		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count) 
  
			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {} 
  
				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                
				#appending parsed tweet to tweet list
				if tweet.retweet_count > 0:
					#if tweet is retweeted, ensure it is appended only once
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			
			#return parsed tweets
			return tweets
			
		except tweepy.TweepError as e:
			#print errors if any
			print("Error:"+str(e))
	
			
#main function
def main():
	#create object of TwitterClient Class
	api = TwitterClient()
	#calling functions to get tweets
	tweets = api.get_tweets(query = 'Donald Trump', count = 200)
	
	#picking positive tweets from tweets
	ptweets = [tweet for tweet in tweets if tweet['sentiment']=='positive']
	#percentage of positive tweets
	print("Positive tweets percentage : {}%".format(100*len(ptweets)/len(tweets)))
    
    #picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    #percentage of negative tweets
    print("Negative tweets percentage : {}%".format(100*len(ntweets)/len(tweets)))
    
    #percentage of neutral tweets
    print("Neutral tweets percentage: {}% \".format(100*len(tweets - ntweets - ptweets)/len(tweets)))
    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
			
		
