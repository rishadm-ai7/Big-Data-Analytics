import tweepy
import os
from textblob import TextBlob

os.chdir('/home/rishad/pyspark_stream')
# to change the directory of the data being saved
#the data which comes from the server is in the json format.
save_file = open("twitter.json",'a')

# step1: Authentication :-
consumer_key='6Zzs9MhyJwmmD2izCxwFsNedi'
consumer_secret='npuzy7Xx98i9Qa0RdHoiSlugTe60AFkedaPLUMRLrIbtDW8Gsk'
access_token='1456242151667367940-NfTp2qC0gA35bhFwUVf74wg7RO32ZH'
access_secret='ER1rLXhrw7vgQXTOOQ2FEBHyzBwRAoR0O4zf31xeO64OD'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)
# step2: api
api = tweepy.API(auth)

# step3: Retrieve tweets
public_tweets = api.search_tweets('farm laws',count=200)

for tweets in public_tweets:
    print(tweets.text)

# step4: Perform sentiment analysis
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)

save_file.write(str(public_tweets))
save_file.close()