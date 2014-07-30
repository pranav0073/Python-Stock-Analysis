# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 00:47:16 2014

@author: Pranav
"""

import urllib2
import time
import datetime

StocksToPull = 'ITC.NS','BHEL.NS','idfc.NS'

def pullData(stock):
    try:
        print 'currently puling', stock
        print str(datetime.datetime.fromtimestamp(time.time()))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        #alt = 'localhost/ITC.csv'  
        saveFileLine = stock+'.txt'
        try:
            readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
            lastUnix = mostRecentLine.split(',')[0]
            
        except Exception,e:
            print str(e)
            lastUnix = 0
        
        saveFile = open(saveFileLine,'a')
        SourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = SourceCode.split('\n')
        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6:
                if  splitLine[0] > lastUnix:
                    if 'values' not in eachLine:
                        lineToWrite = eachLine+'\n'
                        saveFile.write(lineToWrite)
        saveFile.close()
        print 'pulled', stock
        print 'sleeping'
        time.sleep(5)


            
    except Exception,e:
        print "main loop fail "

for eachStock in StocksToPull:
    pullData(eachStock);