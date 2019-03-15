import xmlrpc.client 
from scipy.io import wavfile
import numpy as np
import os

# Initiate the memcached database
# os.system("memcached")

machine1 = xmlrpc.client.ServerProxy('http://0.0.0.0:8000')

fs, data = wavfile.read('./machine_0_test.wav')

final_result = machine1.audio_analysis(fs, np.ndarray.tolist(data))

print(final_result)