class Listener:
    def __init__(self, consumer):
        self.consume = consumer

    def on_data(self, tweet_in_json):
        self.consume(tweet_in_json)

    def on_connect(self):
        print "Connect to twitter stream."

    def on_exception(self, exception):
        print "Encounter expcetion " + str(exception)

    def on_error(self, status_code):
        print "Encounter error with code " + str(status_code)