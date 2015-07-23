import tweepy,json,datetime,tabulate,requests,urllib2,urlunshort
from ttp import ttp
from urlparse import urlparse
from collections import Counter

keyword = raw_input("Enter the Keyword for Text mining!")

consumer_key = 'Ub65AhEo1MHZVvUwYmTa6lIrk'
consumer_secret = 'uoHB1MKFQvgsPZTaiIvL9mtLO1ngxLKOzRkDmNvYy5iTOaZWTR'
access_token = '1393043094-wtXc46OEZ8rdaAhzvbNcp53McqcZrFq3C38HAPa'
access_token_secret = 'XixqcLDMrWQI6dVNByYr4sUfOPjFKTtAZbfZgSI2CTLlu'
k,text,seq,seq2=[],[],[],[]
sched = datetime.datetime.now()
interval = 1
print "Time now is -->",sched

class StdOutListener(tweepy.StreamListener):
    
    def on_data(self, data):
        global k,sched,interval,text,seq,seq2
        decoded = json.loads(data)
        date_tweet = datetime.datetime.fromtimestamp(int(decoded['timestamp_ms'])/1e3)+datetime.timedelta(0,5.5)
        k.append([[decoded['user']['screen_name'].encode('utf-8')] ,date_tweet.strftime('%Y-%m-%d %H:%M:%S')])
        count = len(text)
        text.append(decoded['text'])
        seq.extend(ttp.Parser().parse(i).urls for i in text[count:] if ttp.Parser().parse(i).urls and i)
        print "-->",
        if (date_tweet)-sched >= datetime.timedelta(minutes=interval) and interval <=3:
            print "\n"," Report for minute :",interval
            print tabulate.tabulate(k),"\n"
            interval +=1
        elif interval==4:            
            print "Printing top 10 Domains By Count:"
            url_count = Counter([i[0] for i in seq])
            for p in sorted(url_count.viewkeys()):
                try:
                    seq2.extend([(urlparse(urllib2.urlopen(p).url).netloc).encode('utf-8')])
                except urllib2.HTTPError:
                    pass
            print Counter(seq2).most_common(10)
##            for i in set(seq):
##                try:
##                    seq2.extend([(urlparse(urllib2.urlopen(i[0]).url).netloc).encode('utf-8')])
##                except urllib2.HTTPError,AttributeError:
##                    pass
##                except KeyboardInterrupt:
##                    print "Thanks for Using!"
##            print Counter(seq2).most_common(10)
            return False        
    def on_error(self, status):
        print status

l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print "Showing new Users for '%s':"%(keyword)
stream = tweepy.Stream(auth, l)
stream.filter(track=[keyword])

