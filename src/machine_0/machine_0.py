import xmlrpc.client 
from scipy.io import wavfile
import numpy as np
import os

# Initiate the memcached database
# os.system("memcached")

machine1 = xmlrpc.client.ServerProxy('http://0.0.0.0:8000')

fs, data = wavfile.read('machine_0_test.wav')

final_result = machine1.audio_analysis(fs, np.ndarray.tolist(data))

# Expected Result:
# A list of tuples, each is the analysis result for one sentence from the audio file.
# For example, if the audio consists of ten sentences, the final result should be a list of 10 tuples.

print(final_result)