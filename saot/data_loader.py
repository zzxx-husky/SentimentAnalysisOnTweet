import cPickle as pk
import csv
import os

from cleaner import Cleaner


class Dataset:
    def __init__(self):
        self.data = []
        self.query = []
        self.target = []

    def clean(self):
        self.data = map(Cleaner.clean, self.data, self.query)
        # remove None samples
        while (None in self.data):
            idx = self.data.index(None)
            del self.data[idx]
            del self.target[idx]
            del self.query[idx]

    @staticmethod
    def load_data(path, delimiter=',', quotechar='"', cached=True):
        pkpath = path + ".pkl"
        if cached and os.path.isfile(pkpath):
            print "Loading from pickle file " + pkpath
            with open(pkpath, "rb") as bin:
                ds = pk.load(bin)
        else:
            print "Loading dataset " + path
            ds = Dataset()
            with open(path, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
                for row in spamreader:
                    ds.target.append(int(row[0].strip('"')))
                    ds.query.append(row[3].strip('"').lower())
                    ds.data.append(row[5].strip('"'))
            assert len(ds.target) == len(ds.query) and len(ds.target) == len(ds.data)
            print "Cleaning dataset " + path
            ds.clean()
            if cached:
                print "Writing to pickle file " + pkpath
                with open(pkpath, "wb") as bin:
                    pk.dump(ds, bin)
        return ds
