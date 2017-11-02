import numpy as np

from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

from cleaner import Cleaner
from config import Config
from downloader import Downloader
from listener import Listener
from data_loader import *
import tfidf


def consume(tweet):
    print tweet.author.id_str, tweet.text


if __name__ == '__main__':
    # Downloader(Config.parse("saot.config")).start_searching(["alphago zero"], Listener(consume))
    ds = load_data('../data/training.1600000.processed.noemoticon.csv')
    ds.clean()

    # 15% data for test
    data_train, data_test, y_train, y_test = train_test_split(ds.data, ds.target, test_size=0.15)

    # Apply tf-idf
    # Prune words if df is strictly smaller than 2 (i.e., appearing in only 1 doc),
    # and words that appears in strictly more than 95% of docs (may need to be tuned)
    tfidfVectorizer = tfidf.build_tfidf(min_df=2, max_df=0.95)
    X_train = tfidfVectorizer.fit_transform(data_train)
    print('Number of samples: %i' % len(data_train))
    print('Number of features: %i' % len(tfidfVectorizer.vocabulary_))
    print('\t%i words are pruned.\n' % len(tfidfVectorizer.stop_words_))

    svm_clf = LinearSVC(dual=False, C=1.0)
    svm_clf.fit(X_train, y_train)
    predicted = svm_clf.predict(tfidfVectorizer.transform(data_test))
    print('Accuracy: %f' % np.mean(predicted == y_test))