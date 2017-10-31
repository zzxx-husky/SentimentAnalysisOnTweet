import sys

from config import Config
from downloader import Downloader
from listener import Listener

if __name__ == '__main__':
    config = Config.parse("saot.config")
    downloader = Downloader(config)
    downloader.start_streaming(["alphago", "zero"], Listener(sys.stdout.write))
