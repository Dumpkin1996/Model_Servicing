from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from scipy.io import wavfile
from pymemcache.client import base
import numpy as np
import os


def audio_analysis(fs, audio_data):

	# Define file names
	local_audio_file_name = "machine_1_test.wav"
	local_text_file_name = "machine_1_test.txt"

	# Save the audio file passed up from machine 0 locally.
	wavfile.write(local_audio_file_name, fs, np.asarray(audio_data, dtype=np.int16))

	# MAIN: Do my work as machine 1. (I am a transcriber.)
	if not os.path.isfile(local_text_file_name):
		command = "pocketsphinx_continuous -infile " + local_audio_file_name + " > " + local_text_file_name
		os.system(command)	
	with open(local_text_file_name, "r") as text_file:
		text_data = text_file.read().replace('\n', '')

	# Save my work result at the remote databse to remedy future data corruption
	memcahced_client = base.Client(('localhost', 11211))
	memcahced_client.set("test", text_data)

	# Call machine 2 to finish all the rest work and get back the result for machine 0.
	machine2 = xmlrpc.client.ServerProxy('http://0.0.0.0:9000')
	text_data = "CORRUPTED"  # Test the database recovery functionality.
	text_analysis_result = machine2.text_analysis(text_data)

	return text_analysis_result


server = SimpleXMLRPCServer(("0.0.0.0", 8000))

print("Listening on port 8000...")

server.register_function(audio_analysis, "audio_analysis")

server.serve_forever()