
import re

pos = []
neg = []
split = re.compile("\\W").split

def newtweet(tweet):
    if tweet.startswith("[0]"):
        neg.append(tweet[4:])
    else:
        pos.append(tweet[4:])

def topwords(coll):
    wmap = {}
    for tweet in coll:
        words = [i.strip() for i in split(tweet.lower()) if len(i.strip()) > 1]
        for i in range(len(words)):
            w = words[i]
            wmap[w] = (wmap[w] + 1) if wmap.has_key(w) else 1
            if i != 0:
                w = words[i - 1] + ' ' + words[i]
                wmap[w] = (wmap[w] + 1) if wmap.has_key(w) else 1
    return wmap

if __name__ == '__main__':
    with open("trump.bak", "r") as datafile:
        buf = None
        for line in datafile:
            if line.startswith("[0]") or line.startswith("[4]"):
                if buf: newtweet(buf)
                buf = ""
            buf += line
        if buf: newtweet(buf)

    print "pos: ", len(pos), "neg: ", len(neg)

    pmap = topwords(pos)
    nmap = topwords(neg)

    # ptop = sorted(pmap, key = pmap.get, reverse = True)[200]
    ntop = sorted(nmap, key = nmap.get, reverse = True)[:500]

    # print "pos tops:", ptop
    print "neg tops:", ntop

    pmap.update(nmap)
    ttop = sorted(pmap, key = pmap.get, reverse = True)[:200]

    print "overall tops:", ttop

    keys = ['flynn', 'fbi', 'amp', 'tax', 'abc', 'russia', 'obama', 'comey', 'fake', 'america', 'the fbi', 'gop', 'foxnews', 'potus', 'lawyer', 'report', 'hillary', 'lying', 'election', 'clinton', 'mueller', 'fake news', 'bill', 'cnn', 'michael', 'money', 'anti trump', 'brian', 'brian ross', 'administration', 'war', 'american', 'dowd', 'white house', 'putin', 'collusion', 'fox', 'abc news', 'media', 'law', 'liar', 'truth', 'racist', 'fuck', 'state', 'republicans', 'americans', 'bush', 'of justice', 'maga', 'russian', 'tax bill', 'suspends', 'thehill', 'trump supporters', 'corrupt', 'presidency', 'fact', 'korea', 'trump lawyer', 'senate', 'the election', 'jail', 'usa', 'flynn guilty', 'party', 'the people', 'flynn lied', 'comey to', 'trump administration', 'ross over', 'trump flynn', 'poor', 'dems', 'market', 'email', 'campaign', 'congress', 'fire', 'he fired', 'email', 'elected', 'idiot', 'against trump', 'russians', 'trump tweet', 'fucking', 'traitor', 'republican', 'pence', 'security', 'firing', 'stock', 'sexual', 'russia probe', 'north', 'hell']
    for key in keys:
        print key, nmap[key]