from config import Config
from downloader import Downloader


class Printer:
    def on_data(self, data):
        print data
        return True

    def on_connect(self):
        print "Connect to twitter stream successfully"

    def on_exception(self, exception):
        print "Encounter error with exception " + str(exception)

    def on_error(self, status_code):
        print "Encounter error with status code " + str(status_code)


if __name__ == '__main__':
    config = Config.parse("saot.config")
    downloader = Downloader(config)
    downloader.start_searching(["alphago zero"], Printer())
