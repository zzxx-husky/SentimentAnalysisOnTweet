import os
import subprocess

mkdir = lambda dir: subprocess.call(["mkdir", dir]) == 0
hasdir = os.path.isdir
hasfile = os.path.exists
hascmd = lambda cmd: len(subprocess.check_output(["which", cmd])) != 0
rmfile = lambda file: subprocess.call(["rm", file])


class Sentiment140:
    def __init__(self):
        dir = "../sentiment140/"
        url = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
        arc = "trainingandtestdata.zip"
        train = "training.1600000.processed.noemoticon.csv"
        test = "testdata.manual.2009.06.14.csv"
        if not hasdir(dir):
            if not mkdir(dir) or not hasdir(dir):
                raise Exception("Failed to create directory: " + dir)
        os.chdir(dir)
        if not hasfile(train) or not hasfile(test):
            if not hasfile(arc):
                if not hascmd("wget"):
                    raise Exception("Command `wget` is not supported. Cannot download the Sentiment140 dataset")
                if subprocess.call(["wget", url]) != 0 or not hasfile(arc):
                    raise Exception("Failed to download the Sentiment140 dataset.")
            if not hascmd("unzip"):
                raise Exception("Command `unzip` is not supported. Cannot unarchive the Sentiment140 dataset")
            if subprocess.call(["unzip", arc]) != 0 or not hasfile(train) or not hasfile(test):
                raise Exception("Failed to unarchive the Sentiment140 dataset.")
            rmfile(arc)
        self.train_path = os.path.abspath(train)
        self.test_path = os.path.abspath(test)
