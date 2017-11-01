from cleaner import Cleaner
from config import Config
from downloader import Downloader
from listener import Listener


def consume(tweet):
    print tweet.author.id_str, tweet.text


if __name__ == '__main__':
    Downloader(Config.parse("saot.config")).start_searching(["alphago zero"], Listener(consume))
