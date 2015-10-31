from streamReader import streamReader
from words import words

ONLINE = 0

def post_tweets(l):
    for s in l:
        print s

def main():
    tweets = []

    # read from db
    reader  = streamReader()
    trends = reader.getTrends()
    # feed contents with each tag into words to form dictionary
    for tr in trends:
        data = reader.getTweets(tr)
        learner = words()
        for text in data:
            learner.add_sentence(text)
        tweets.append(learner.gen_sentence(140))

    # generate the sentence within the length limit of tweets

    # output method
    if ONLINE:
        post_tweets(tweets)

if __name___ == '__main__':
    main()