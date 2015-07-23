import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time

date,bid,ask = np.loadtxt('GBPUSD1d.txt',unpack=True,delimiter=',',
                            converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
    
def percentChange(startpoint,currentpoint):
    return float(((currentpoint-startpoint)/startpoint)*100)

def patternFinder():
    avgline = ((bid+ask)/2)
    x= len(avgline)-30
    y=11
    while y<x:
        p1 = percentChange(avgline[y-10],avgline[y-9])
        p2 = percentChange(avgline[y-10],avgline[y-9])
        p3 = percentChange(avgline[y-10],avgline[y-9])
        p4 = percentChange(avgline[y-10],avgline[y-9])
        p5 = percentChange(avgline[y-10],avgline[y-9])
        p6 = percentChange(avgline[y-10],avgline[y-9])
        p7 = percentChange(avgline[y-10],avgline[y-9])
        p8 = percentChange(avgline[y-10],avgline[y-9])
        p9 = percentChange(avgline[y-10],avgline[y-9])
        p10 = percentChange(avgline[y-10],avgline[y-9])

        outcomeRange = avgline[y+20:y+30]
        currentPoint = avgline[y]
        print reduce(lambda x, y:x+y,outcomeRange)/len(outcomeRange)
        print currentPoint
        print '----------'
        print p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
        y+=1
        time.sleep(120)
        
        
    
    
    

def graphRawFX():


    fig=plt.figure(figsize=(10,7))
    ax1=plt.subplot2grid((40,40),(0,0),rowspan = 40,colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date,0,(ask-bid),facecolor='g',alpha=0.3)
    plt.subplots_adjusts(bottom=.23)
    
    plt.grid(True)
    plt.show()


    

