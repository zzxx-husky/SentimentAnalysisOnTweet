import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

from stop_words import *

class TFIDF(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        english_stemmer = nltk.stem.SnowballStemmer('english')
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

    @staticmethod
    def build(min_df=2, max_df=0.95, stop_words=ENGLISH_STOP_WORDS):
        return TFIDF(min_df=min_df,
                     max_df=max_df,
                     stop_words=stop_words,
                     norm='l2',
                     sublinear_tf=True)
