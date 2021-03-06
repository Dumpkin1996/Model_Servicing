#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:22:54 2019

@author: davidzhou
"""

import numpy as np
import tensorflow as tf
import re
#from xmlrpclib import ServerProxy
import xmlrpc.client as xmlrpclib
from xmlrpc.server import SimpleXMLRPCServer

batchSize = 24
lstmUnits = 64
numClasses = 2
numDimensions=50
maxSeqLength=250
strip_special_chars = re.compile("[^A-Za-z0-9 ]+")

def cleanSentences(string):
    string = string.lower().replace("<br />", " ")
    return re.sub(strip_special_chars, "", string.lower())

wordsList = np.load('wordsList.npy')
print('Loaded the word list!')
wordsList = wordsList.tolist() #Originally loaded as numpy array
wordsList = [word.decode('UTF-8') for word in wordsList] #Encode words as UTF-8
wordVectors = np.load('wordVectors.npy')


#paragraph is a string
def sentimental_analysis(paragraph):
    ids = np.zeros((1, maxSeqLength), dtype='int32')
    indexCounter = 0
    cleanedLine = cleanSentences(paragraph)
    split = cleanedLine.split()
    for word in split:
        try:
            ids[0][indexCounter] = wordsList.index(word)
        except ValueError:
                ids[0][indexCounter] = 399999 #Vector for unkown words
                indexCounter = indexCounter + 1
                if indexCounter >= maxSeqLength:
                    break
    tf.reset_default_graph()
    
    labels = tf.placeholder(tf.float32, [24, numClasses])
    input_data = tf.placeholder(tf.int32, [24, maxSeqLength])
    
    data = tf.Variable(tf.zeros([batchSize, maxSeqLength, numDimensions]),dtype=tf.float32)
    data = tf.nn.embedding_lookup(wordVectors,input_data)
    
    lstmCell = tf.nn.rnn_cell.LSTMCell(lstmUnits)
    lstmCell = tf.contrib.rnn.DropoutWrapper(cell=lstmCell, output_keep_prob=0.75)
    value, _ = tf.nn.dynamic_rnn(lstmCell, data, dtype=tf.float32)
    
    weight = tf.Variable(tf.truncated_normal([lstmUnits, numClasses]))
    bias = tf.Variable(tf.constant(0.1, shape=[numClasses]))
    value = tf.transpose(value, [1, 0, 2])
    last = tf.gather(value, int(value.get_shape()[0]) - 1)
    prediction = (tf.matmul(last, weight) + bias)
    correctPred = tf.equal(tf.argmax(prediction,1), tf.argmax(labels,1))
    
    with tf.Session() as sess:
        # Restore variables from disk.
        #saver = tf.train.import_meta_graph('models1/pretrained_lstm.ckpt-99.meta')
        saver=tf.train.Saver()
        saver.restore(sess,tf.train.latest_checkpoint('models1/'))
        inputdt=np.zeros([batchSize,maxSeqLength])
        lb=[]
        for i in range(batchSize):
            lb.append([1,0])
            inputdt[i]=ids[0]
        Prediction=sess.run(correctPred[0], {input_data: inputdt, labels: lb})
        print("Prediction: ", Prediction)
        sess.close()
        if Prediction:
            return 1;
        else:
            return 0;

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("Listening on port 8000...")
server.register_function(sentimental_analysis, "sentimental_analysis")
server.serve_forever()
      
  
  
  







    
    
    
    
    
    