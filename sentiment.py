
import re
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import matplotlib.pyplot as plt
import json

class TwitterClient(object):
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
       
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'positive'
        else:
            return 'negative'
    def read_tweets(self):
        tweets_list=[]
        with open('jerusalem.json', 'r') as file:
            for line in file:
                #print(line)
                try:
                    tweet = json.loads(line)
                    #print(tweet['text'])
                    #terms_all = [term for term in preprocess(tweet['text'])]
                    tweets_list.append(tweet['text'])
                    #print(tweets_list[i])
                    #i=i+1
                except BaseException as e:{}
        return tweets_list
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            #fetched_tweets = self.api.search(q = query, count = count)
            fetched_tweets=self.read_tweets()
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet)
 
                # appending parsed tweet to tweets list
                #if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                 #   if parsed_tweet not in tweets:
                  #      tweets.append(parsed_tweet)
                #else:
                tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 

api = TwitterClient()
tweets = api.get_tweets(query = 'Jerusalem', count = 500)
 
ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
posPerc=format(100*len(ptweets)/len(tweets))
ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
negPerc=format(100*len(ntweets)/len(tweets))
y=(len(ptweets),len(ntweets))
x=(0,len(tweets))

print("\n\nPositive tweets:")
for tweet in ptweets[:20]:
    print(tweet['text'])
 
print("\n\nNegative tweets:")
for tweet in ntweets[:20]:
    print(tweet['text'])

print("\n")
print("Positive tweets percentage: {} % "+posPerc)
print("Negative tweets percentage: {} % "+negPerc)
