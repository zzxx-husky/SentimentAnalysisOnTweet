import re


class Cleaner:
    @staticmethod
    def clean(text, query_term='no_query'):
        # 0. Retweet without comment, sentiment = author's sentiment; Retweet with comment, sentiment = comment's sentiment.
        idx = text.find('RT @')
        if idx >= 0:
            text = text[:idx]
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