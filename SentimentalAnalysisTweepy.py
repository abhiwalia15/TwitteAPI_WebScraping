import re
import tweepy
from tweepy import OAuthHandler
#from textblob import Textblob

class TwitterCliend(object):
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
			
		
