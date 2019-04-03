#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:29:29 2019

@author: davidzhou
"""
#rpc package
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer

#text is a list of words
def subject_analysis(texts):
    #connect to tokenizor
    #address need to be adjusted
    tokenizor = xmlrpc.client.ServerProxy('http://0.0.0.0:14000')
    wordsList = tokenizor.text_clean(texts)
    
    #do simple analysis
    d={}
    count=0
    for word in wordsList:
        if word not in d:
            d[word]=0
        d[word]+=1
        count+=1
    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))
    word_freq.sort(reverse=True)

    subject_analysis_result = ""
    subject_analysis_result += "Total number of words: " + str(count) + "\n"
    subject_analysis_result += "Top three frequent words: (count, word)"
    subject_analysis_result += word_freq[:3]
    
    return subject_analysis

server = SimpleXMLRPCServer(("0.0.0.0", 13000))

print("Listening on port 13000...")

server.register_function(subject_analysis, "subject_analysis")

server.serve_forever()
    
        