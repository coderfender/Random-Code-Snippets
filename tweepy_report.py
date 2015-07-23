import time,tweepy,tabulate,datetime,requests
from threading import Timer
from ttp import ttp

key_word = raw_input("Enter the KeyWOrd for text mining! ")
d= datetime.datetime.now()
print "Time now is: ",d
consumer_key = 'Ub65AhEo1MHZVvUwYmTa6lIrk'
consumer_secret = 'uoHB1MKFQvgsPZTaiIvL9mtLO1ngxLKOzRkDmNvYy5iTOaZWTR'
access_token = '1393043094-wtXc46OEZ8rdaAhzvbNcp53McqcZrFq3C38HAPa'
access_token_secret = 'XixqcLDMrWQI6dVNByYr4sUfOPjFKTtAZbfZgSI2CTLlu'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

sched = 1


def Twitter_Feed(keyword,sched):
     k=[]
     
     while datetime.datetime.now()-d<datetime.timedelta(minutes=5):
          k = k +[[i.created_at,datetime.datetime.now(),i.user.screen_name,i.user.statuses_count,i.text] \
               for i in tweepy.Cursor(api.search,q=keyword,count=10).items(20) \
               if (i.created_at+datetime.timedelta(0,5.5)) -datetime.datetime.now()<datetime.timedelta(seconds=sched)]
          print tabulate.tabulate(k)

          sched +=10
          print "Fetching Data for minute",sched,"...."
          
          time.sleep(60)
     else:
          t = ttp.Parser()
          print "The URLS Embedded in the tweets are",
##          print tabulate.tabulate([t.parse(url[4]).urls for url in k])
##          for u in xrange(0,len(k)):                         
##                          print str(ttp.Parser().parse(k[u][4]).urls),
          url_list= [((str(ttp.Parser().parse(k[u][4]).urls[0]),requests.get((ttp.Parser().parse(k[u][4]).urls)[0]).url)) for u in xrange(0,len(k)) if ttp.Parser().parse(k[u][4]).urls ]
          print tabulate.tabulate(url_list)

Twitter_Feed(key_word,sched)
        

    

