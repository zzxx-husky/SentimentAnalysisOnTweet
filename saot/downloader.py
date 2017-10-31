import threading
import time

import tweepy


class Downloader:
    def __init__(self, config):
        self.auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
        self.auth.set_access_token(config["access_token"], config["access_token_secret"])

    def start_searching(self, keywords, listener):
        def listen():
            api = tweepy.API(self.auth)
            last_id = -1
            while True:
                try:
                    # start searching from the oldest tweets that can be achieved
                    new_tweets = api.search(q=keywords, count=100, max_id=str(last_id))
                    if len(new_tweets) > 0:
                        last_id = new_tweets[-1].id - 1
                        for i in new_tweets: listener.on_data(i)
                    else:
                        print "No new search results. Try after 5 seconds..."
                        time.sleep(5)
                except tweepy.TweepError as e:
                    print "Exception caught: " + str(e) + ". Stopping twitter searching."
                    break

        threading.Thread(target=listen).start()

    def start_streaming(self, keywords, listener):
        tweepy.Stream(self.auth, listener).filter(track=keywords, async=True)
