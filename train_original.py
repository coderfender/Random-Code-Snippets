import urllib2
import json
import time
##train_no = str(raw_input("Please enter the train number "))
##d = str(raw_input("Please enter the DATE OF JOURNEY in YYYYMMDD format (Hit Enter for today!))")) or time.strftime('%Y%m%d')

def train(train_no):    
    apikey = 89321

    try:
    
        if( 00116 < int(train_no) < 84370):
            url = 'http://api.railwayapi.com/live/train/%s/doj/%s/apikey/10270'%(train_no,d)
            #url2= 'http://api.railwayapi.com/route/train/%s/apikey/10270/' %d
            #print url
            json_data= urllib2.urlopen(url)
            #json_data2= urllib2.urlopen(url2)
            data = json.load(json_data)
            #data2 = json.load(json_data2)
            print "No of stops are:",len(data['route'])
            print data["position"]
            #for i in range(0,len(data2['route'])):
                #print data2['route'][i]['code'],data2['route'][i]['fullname'],data2['route'][i]['state']
            for i in range(0,len(data['route'])):                    
                print data['route'][i]['station'],":",data['route'][i]['status'],"time :",data['route'][i]['actarr']
            print "*"*30

        else:
            print "The train number entered is invalid"

    except ValueError:
        print ("Invalid entry! Please try again")

    except KeyError:
        print "Maximum hits reached!Try after 24 hrs!"
    except KeyboardInterrupt:
        print "Thanks asshole!Get the fuck outta here!"


    
try:
    while True:
            train(train_no)
            time.sleep(10)
except KeyboardInterrupt:
        print "Thanks asshole!Get the fuck outta here!"
