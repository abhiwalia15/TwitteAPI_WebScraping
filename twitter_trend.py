# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1050006838366810112-vayi2L8Q1vxbPbUOdibmw7CYQhb72g'
ACCESS_SECRET = 'V4cCohGfJa30T8agz5LgStpNUqDetXbEmWjjSaiC8bpJc'
CONSUMER_KEY = 'H09lz1MRceBRko8xt86OIlv5i'
CONSUMER_SECRET = 'MtDWYPzXUxhEXfL5HQcKSSig0ncynEprZfyTJ7hIezHISWSOTa'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter = Twitter(auth=oauth)

world_trends = twitter.trends.place(_id=23424848)

print(json.dumps(world_trends, indent=4))
print('--------------------')

i=0
while i<10:
	print(world_trends[0]['trends'][i]['name'])
	print(world_trends[0]['trends'][i]['url'])
	print(world_trends[0]['trends'][i]['promoted_content'])
	print(world_trends[0]['trends'][i]['query'])
	print(world_trends[0]['trends'][i]['tweet_volume'])
	i=i+1
