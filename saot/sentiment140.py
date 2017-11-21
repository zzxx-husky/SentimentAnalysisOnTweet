import os
import sys
import urllib
import zipfile

mkdir = os.makedirs
hasdir = os.path.isdir
hasfile = os.path.exists
rmfile = os.remove
download = urllib.request.urlretrieve if sys.version[0] == 3 else urllib.urlretrieve


class Sentiment140:
    def __init__(self):
        dir = "../sentiment140/"
        url = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
        arc = "trainingandtestdata.zip"
        train = "training.1600000.processed.noemoticon.csv"
        test = "testdata.manual.2009.06.14.csv"
        if not hasdir(dir):
            mkdir(dir)
            if not hasdir(dir):
                raise Exception("Failed to create directory: " + dir)
        cur_dir = os.getcwd()
        os.chdir(dir)
        if not hasfile(train) or not hasfile(test):
            if not hasfile(arc):
                download(url, arc)
                if not hasfile(arc):
                    raise Exception("Failed to download the Sentiment140 dataset.")
            with zipfile.ZipFile(arc, "r") as zip:
                zip.extractall(".")
            if not hasfile(train) or not hasfile(test):
                raise Exception("Failed to unarchive the Sentiment140 dataset.")
            rmfile(arc)
        self.train_path = os.path.abspath(train)
        self.test_path = os.path.abspath(test)
        os.chdir(cur_dir)
