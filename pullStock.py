# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 00:47:16 2014

@author: Pranav
"""

import urllib2
import time

StockToPull = "ITC.NS"

def pullData(stock):
    try:
        fileLine = stock+'.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        print sourceCode
    except Exception,e:
        print "main loop fail "+(e)
pullData(StockToPull);