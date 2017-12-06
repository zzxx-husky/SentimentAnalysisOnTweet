import cPickle as pk

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

from cleaner import Cleaner
from config import Config
from data_loader import Dataset
from downloader import Downloader
from listener import Listener
from sentiment140 import Sentiment140
from tfidf import TFIDF
from visualizer import Visualizer

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

    try:
        with open("svm.pkl", "rb") as bin:
            svm = pk.load(bin)
        print "Successfully loaded svm model"
    except:
        svm = LinearSVC(dual=False, C=1.0)
        svm.fit(X_train, y_train)
        with open("svm.pkl", "wb") as bin:
            pk.dump(svm, bin)
    predicted_train = svm.predict(tfidf.transform(data_train))
    print('Accuracy: %f' % np.mean(predicted_train == y_train))
    predicted_test = svm.predict(tfidf.transform(data_test))
    print('Accuracy: %f' % np.mean(predicted_test == y_test))

    visual = Visualizer(table_names=["summary", "percentage"])
    pos, neg, summ_cnt = 0, 0, 0

    def consume(tweet):
        global summ_cnt, pos, neg
        clean = Cleaner.clean(tweet.full_text)
        if clean is not None:
            tran = tfidf.transform([clean])
            pred = svm.predict(tran)
            print pred, tweet.full_text.encode('utf-8')

            summ_cnt += 1
            if pred == 4: pos += 1
            if pred == 0: neg += 1
            visual.add_data("summary", summ_cnt, pos, 0)
            visual.add_data("summary", summ_cnt, neg, 1)
            visual.add_data("percentage", summ_cnt, float(pos) / summ_cnt, 0)
            visual.add_data("percentage", summ_cnt, float(neg) / summ_cnt, 1)


    Downloader(Config.parse("saot.config")).start_searching(["trump"], Listener(consume))
