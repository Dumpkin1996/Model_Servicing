import os
import xmlrpc.client
import numpy as np
import speech_recognition as sr
from os import path
from xmlrpc.server import SimpleXMLRPCServer
from scipy.io import wavfile
from pymemcache.client import base

def audio_analysis(fs, audio_data):

	# Define file names
	local_audio_file_name = os.path.join(path.dirname(path.realpath(__file__)), "machine_1_test.wav")

	# Save the audio file passed up from machine 0 locally.
	wavfile.write(local_audio_file_name, fs, np.asarray(audio_data, dtype=np.int16))

	# MAIN: Do my work as machine 1. (I am a transcriber.)
	r = sr.Recognizer()
	with sr.AudioFile(local_audio_file_name) as source:
		audio = r.record(source)     # read the entire audio file
	try:
	    text_data = r.recognize_sphinx(audio)
	except sr.UnknownValueError:
	    print("Sphinx could not understand audio")
	except sr.RequestError as e:
	    print("Sphinx error; {0}".format(e))

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