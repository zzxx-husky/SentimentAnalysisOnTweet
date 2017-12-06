import cPickle as pk

import numpy as np
import torch
from sklearn.model_selection import train_test_split

from cleaner import Cleaner
from config import Config
from data_loader import Dataset
from downloader import Downloader
from listener import Listener
from nn import NeuralNetwork
from sentiment140 import Sentiment140
from tfidf import TFIDF
from visualizer import Visualizer


def to_torch_sparse_tensor(M):
    """Convert Scipy sparse matrix to torch sparse tensor."""
    M = M.tocoo().astype(np.float32)
    indices = torch.from_numpy(np.vstack((M.row, M.col))).long()
    values = torch.from_numpy(M.data)
    shape = torch.Size(M.shape)
    return torch.sparse.FloatTensor(indices, values, shape)

if __name__ == '__main__':
    ds = Dataset.load_data(Sentiment140().train_path)

    # 15% data for test
    data_train, data_test, y_train, y_test = train_test_split(ds.data, ds.target, test_size=0.15)

    # Apply tf-idf
    # Prune words if df is strictly smaller than 2 (i.e., appearing in only 1 doc),
    # and words that appears in strictly more than 95% of docs (may need to be tuned)
    try:
        with open("tfidf.pkl", "rb") as bin:
            (tfidf, X_train) = pk.load(bin)
        print "Successfully loaded tfidf model"
    except:
        tfidf = TFIDF.build(min_df=2, max_df=0.95)
        X_train = tfidf.fit_transform(data_train)
        with open("tfidf.pkl", "wb") as bin:
            pk.dump((tfidf, X_train), bin)
    print('Number of samples: %i' % len(data_train))
    print('Number of features: %i' % len(tfidf.vocabulary_))
    print('\t%i words are pruned.\n' % len(tfidf.stop_words_))

    net = NeuralNetwork(len(tfidf.vocabulary_), 2)
    net.train(input=to_torch_sparse_tensor(X_train), groundtruth=torch.FloatTensor(y_train))
    predicted_train = net.eval(X_train)
    print('Accuracy: %f' % np.mean(predicted_train == y_train))
    predicted_test = net.eval(tfidf.transform(data_test))
    print('Accuracy: %f' % np.mean(predicted_test == y_test))

    visual = Visualizer(table_names=["summary", "percentage"])
    pos, neg, summ_cnt = 0, 0, 0


    def consume(tweet):
        global summ_cnt, pos, neg
        clean = Cleaner.clean(tweet.full_text)
        if clean is not None:
            tran = tfidf.transform([clean])
            pred = net.predict(tran)
            print pred, tweet.full_text

            summ_cnt += 1
            if pred == 4: pos += 1
            if pred == 0: neg += 1
            visual.add_data("summary", summ_cnt, pos, 0)
            visual.add_data("summary", summ_cnt, neg, 1)
            visual.add_data("percentage", summ_cnt, float(pos) / summ_cnt, 0)
            visual.add_data("percentage", summ_cnt, float(neg) / summ_cnt, 1)


    Downloader(Config.parse("saot.config")).start_searching(["trump"], Listener(consume))
