import csv
from cleaner import Cleaner

class Dataset:
    def __init__(self):
        self.data = []
        self.query = []
        self.target = []

    def clean(self):
        self.data = map(Cleaner.clean_text, self.data, self.query)
        # remove None samples
        while (None in self.data):
            idx = self.data.index(None)
            del self.data[idx]
            del self.target[idx]
            del self.query[idx]


def load_data(path, delimiter=',', quotechar='"'):
    ds = Dataset()
    with open(path, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            ds.target.append(int(row[0].strip('"')))
            ds.query.append(row[3].strip('"').lower())
            ds.data.append(row[5].strip('"'))
    assert len(ds.target) == len(ds.query) and len(ds.target) == len(ds.data)
    return ds
