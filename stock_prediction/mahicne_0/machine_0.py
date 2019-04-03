import xmlrpc.client 
from scipy.io import wavfile
import numpy as np
import os

# Initiate the memcached database
# os.system("memcached")

machine1 = xmlrpc.client.ServerProxy('http://0.0.0.0:8000')

past_stock_index = [100, 200, 300]

def stock_price_retriever():





final_result = machine1.stock_predict(past_stock_index)

# Expected Result:
# A list of strings, each is the analysis result for one sentence from the audio file.
# For example, if the audio consists of ten sentences, the final result should be a list of 10 strings.

print(final_result)