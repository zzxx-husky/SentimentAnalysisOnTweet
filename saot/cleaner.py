import re


class Cleaner:
    @staticmethod
    def clean(tweet):
        id, text = tweet.author.id_str, tweet.text
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

    @staticmethod
    def clean_text(text, query_term='no_query'):
        # 1. remove all short links, e.g. https://t.co/CITaCdl8SU
        text = re.sub(r'http[s]?:/[\S]+', '', text)
        # 2. remove RT @user, e.g. RT @zzxx:
        text = re.sub(r'RT @[\w_]+:', '', text)
        text = re.sub(r'@[\w_]+', '', text)
        # 3. to lower case
        text = text.lower()
        # 4. remove query_term
        if (query_term != 'no_query'):
            text = re.sub(query_term, '', text)
        # 5. replace repeated chars, e.g, huuuungry -> huungry
        text = re.sub(r'([a-zA-Z])\1{2,}', r'\1\1', text)
        # 6. remove useless character, e.g, f**k -> fk, couldn't -> couldnt
        text = re.sub(r'[^a-zA-Z\d\s:]+', '', text)
        text = text.strip()
        return text if len(text) != 0 else None