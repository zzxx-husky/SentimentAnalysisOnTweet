import sys

from saot.config import Config
from saot.downloader import Downloader
from saot.listener import Listener

if __name__ == '__main__':
    config = Config.parse("saot.config")
    downloader = Downloader(config)
    downloader.start_streaming(["alphago", "zero"], Listener(sys.stdout.write))
