from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from pymemcache.client import base
import nltk


def detect_corruption(s):
	return s == "CORRUPTED"

def text_analysis(text):

	# Detect corruption. If corrupted, recover from Database.
	if detect_corruption(text):
		memcahced_client = base.Client(('localhost', 11211))
		text = memcahced_client.get("test")

	# MAIN: Do my work as machine 2. (I am a tokenizer.)
	# print(s)
	sent_list = nltk.sent_tokenize(text)

	# Call machine 3 to finish all the rest work and get back the result for machine 1.
	machine3 = xmlrpc.client.ServerProxy('http://0.0.0.0:11000')
	sentence_analysis_result_list = machine3.sentence_analysis(sent_list)

	return sentence_analysis_result_list


server = SimpleXMLRPCServer(("0.0.0.0", 9000))

print("Listening on port 9000...")

server.register_function(text_analysis, "text_analysis")

server.serve_forever()