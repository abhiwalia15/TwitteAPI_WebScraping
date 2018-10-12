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

#search for the latest tweets about '#nlproc'

iterator = twitter.search.tweets(q='trump', result_type='recent', lang='en', count=10)
print(json.dumps(iterator, indent=4))
