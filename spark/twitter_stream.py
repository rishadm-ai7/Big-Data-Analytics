import tweepy
import os

os.chdir('/home/rishad/pyspark_stream')
# to change the directory of the data being saved
#the data which comes from the server is in the json format.
save_file = open("twitter.json")

# step1: Authentication :-
consumer_key=
consumer_secret=
access_token=
access_secret=

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)




