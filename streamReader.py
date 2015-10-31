from TwitterAPI import TwitterAPI
import PWs
import sqlite3
from time import time

class streamReader:

    def __init__(self):
        self.api = TwitterAPI(PWs.CONSUMER_KEY,
                                    PWs.CONSUMER_SECRET,
                                    PWs.ACCESS_TOKEN_KEY,
                                    PWs.ACCESS_TOKEN_SECRET)

        #Create DB Connection
        self.conn = sqlite3.connect('trendtweets.db')
        self.c = conn.cursor()

    def init_database(self):
        # Create table and index tags
        self.c.execute('''CREATE TABLE tweets
                (tag text, content text)''')

        self.c.execute('CREATE INDEX tag_index \
            on tweets (tag)');

        self.track_trends = self._getTrend()
        for trend in self.track_trends:
            try:
                self._getTweet(trend)
            except Exception, e:
                print 'Error: getting tweet with tag ', trend, ' raised request error: ', e
                continue


    def _getTweet(TRACK_TERM, timeout=1, maxn=10):
        r = self.api.request('statuses/filter', {'track': TRACK_TERM, 'lang': 'en'})

        t = time()
        n = 0

        for item in r:
            if 'text' in item:
                c.execute('INSERT INTO tweets (tag, content) \
                VALUES (?, ?)', (TRACK_TERM, clean_phrase(item['text'])))
            n+=1
            # print(time() - t)
            self.conn.commit()
            if time() - t > timeout: #was 3600
                break
            if n == maxn:
                break

    def _getTrend(self):
        r = api.request('trends/place', {'id': 1, 'lang': 'en'})
        i = 0
        trends = []
        for every in r:
            if every['name'][0] != '#':
                continue
            trends.append(every['name'])
            # if(every['name'][0] == '#') and i != 0:
            #     getTweet(every['name'])
            #     break
            # i += 1
        return trends

    def getTrends(self):
        return self.track_trends

    def getTweets(self, tag):
        cursor = conn.execute("SELECT * FROM tweets WHERE tag = ?", (trend, ))
        return [row[1] for row in cursor]

    def clean_phrase(text):
        return ' '.join([every_word for every_word in text.split(' ') if not ((every_word.startswith(('#', "@", "http"))) or ('#' in every_word) or ('@' in every_word) or every_word == 'RT')])

    def example_1():
        cursor = self.conn.execute("SELECT tag, content from tweets")
        for row in cursor:
               print "TAG = ", row[0]
               print "CONTENT = ", row[1]

    def example_2():
        for trend in self.track_trends:
            cursor = conn.execute("SELECT * FROM tweets WHERE tag = ?", (trend, ))
            print '===============', trend, '==============='
            for row in cursor:
                   print "TAG = ", row[0]
                   print "CONTENT = ", row[1]
            print
