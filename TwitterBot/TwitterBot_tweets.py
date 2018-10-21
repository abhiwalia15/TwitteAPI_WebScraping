#import our Twitter credentials from credentials.py file
from credentials import *
import tweepy 
from time import sleep
from tweepy import OAuthHandler 

#access and authorize our twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#open text file verve.txt for reading

''' ONE WAY OF READING FILES
with open('verve.txt','r') as file_lines:
	my_file = file_lines.readlines()


#print(my_file[:10])
#close file	
file_lines.close()'''

my_file = open('verve.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

def tweet():
	#create a for loop to iterate over file_lines
	for line in file_lines:

	#add try | except block to catch and output errorss
		try:
			print(line)

			#add an if statement to ensure that blank lines are not twetted
			if line!='\n':
				'''for every line to become a new tweet, we use tweepy 
				function api.update_status()'''
				api.update_status(line)

			#add an else statementwith pass to conclude the conditional statement
			else:
				pass

		except tweepy.TweepError as e:
			print(e.reason)	
		#add sleep method to space tweets time by 5 seconds each
		sleep(2)

tweet()












