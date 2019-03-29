import xmlrpc.client
import os

if not os.path.isfile("wandering_earth_1.txt"):
	os.system("pocketsphinx_continuous -infile wandering_earth_1.wav > wandering_earth_1.txt")

with open('wandering_earth_1.txt', 'r') as review1:
  data1 = review1.read().replace('\n', '')

print(data1)

s = xmlrpc.client.ServerProxy('http://0.0.0.0:8000')

print(s.sentimental_analysis(data1)) 