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
        fileName = stock+'.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        #alt = 'localhost/ITC.csv'        
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        
        for eachLine in splitSource:
           splitLine = eachLine.split(',')
           if len(splitLine) == 6:
               if 'values' not in eachLine:
                   saveFile = open(fileName,'a')
                   lineToWrite = eachLine+'\n'
                   saveFile.write(lineToWrite)
        print "stock pulled", stock
        print 'sleeping'
        time.sleep(5)
        
    except Exception,e:
        print "main loop fail "+(e)

for eachStock in StocksToPull:
    pullData(eachStock);