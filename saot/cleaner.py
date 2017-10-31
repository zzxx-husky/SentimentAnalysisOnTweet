import re


class Cleaner:
    @staticmethod
    def clean(tweet):
        id, text = tweet.id, tweet.text
        # 0. handle non-english words: ignore
        # try:
        #     text.decode('ascii') # this may filter too many tweets
        # except UnicodeEncodeError:
        #     # If containing any non-english words, ignore the whole text
        #     return None
        text = text.strip()
        # 1. remove all short links, e.g. https://t.co/CITaCdl8SU
        text = re.sub(r'http[s]?:/[\S]+', '', text)
        # 2. remove RT @user, e.g. RT @zzxx:
        text = re.sub(r'RT @[\w_]+:', '', text)
        text = re.sub(r'@[\w_]+', '', text)
        # 3. remove useless character
        text = re.sub(r'[\W]+', ' ', text)
        # 4. to lower case
        text = text.lower().strip()
        return (id, text) if len(text) != 0 else None
