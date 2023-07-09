# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 08:12:56 2018

@author: Muhammad Umer
"""
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
#import json


class MyListener(StreamListener):
         
    def on_data(self,data):
        print("inside")
        with open('tweets.json', 'a') as f:
            print("writing data")
            #tw=json.loads(data)
            f.write(data)
            return True
    def on_error(self,status):
        print(status)
        return True

auth = OAuthHandler(process.env.CONSUMER_KEY, process.env.CONSUMER_SECRET)
auth.set_access_token(process.env.ACCESS_TOKEN, process.env.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
print("authenticate")
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)
  
twitterStream = Stream(auth, MyListener())
print("hello")
twitterStream.filter(track=['#AskAsadUmar'])

