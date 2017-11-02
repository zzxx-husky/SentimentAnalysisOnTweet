from saot.config import Config
from saot.downloader import Downloader
from saot.listener import Listener


def printdata(tweet):
    print tweet


if __name__ == '__main__':
    config = Config.parse("saot.config")
    downloader = Downloader(config)
    downloader.start_searching(["alphago zero"], Listener(printdata))
