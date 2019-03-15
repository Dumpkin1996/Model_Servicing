from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from pymemcache.client import base


def sentence_analysis(sent_list):
	
	# Connect machine 4 and machine 5.
	machine4 = xmlrpc.client.ServerProxy('http://0.0.0.0:12000')
	machine5 = xmlrpc.client.ServerProxy('http://0.0.0.0:13000')

	# MAIN: Do my work as machine 3. (I am a result-synthesizer.) Combine the output of machine 4 and machine 5.
	sentence_analysis_result_list = []
	for sent in sent_list:
		# Call machine 4 to do sentimental analysis.
		sentimental_analysis_result = machine4.sentimental_analysis(sent)
		# Call machine 5 to do subject analysis.
		subject_analysis_result = machine5.subject_analysis(sent)

		sentence_analysis_result_list.append((sentimental_analysis_result, subject_analysis_result))

	return sentence_analysis_result_list


server = SimpleXMLRPCServer(("0.0.0.0", 11000))

print("Listening on port 11000...")

server.register_function(sentence_analysis, "sentence_analysis")

server.serve_forever()