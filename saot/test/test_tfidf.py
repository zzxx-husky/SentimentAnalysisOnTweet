from saot import data_loader
from saot import tfidf

ds = data_loader.load_data("../../data/test.csv")
ds.clean()

tfidfVectorizer = tfidf.build_tfidf(min_df=1, max_df=1.0, stop_words=None)
tfidfVectorizer.fit(ds.data)
print("Number of features before pruning: %i" % len(tfidfVectorizer.vocabulary_))
print tfidfVectorizer.vocabulary_

tfidfVectorizer = tfidf.build_tfidf(min_df=1, max_df=1.0)
tfidfVectorizer.fit(ds.data)
print("Number of features after stopwords pruning: %i" % len(tfidfVectorizer.vocabulary_))
print tfidfVectorizer.vocabulary_

tfidfVectorizer = tfidf.build_tfidf()
tfidfVectorizer.fit(ds.data)
print("Number of features after all pruning: %i" % len(tfidfVectorizer.vocabulary_))
print tfidfVectorizer.vocabulary_
print("Removed words:")
print tfidfVectorizer.stop_words_
