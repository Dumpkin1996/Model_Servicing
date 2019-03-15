from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from pymemcache.client import base


def subject_analysis(sent):
	
	return 12345678


server = SimpleXMLRPCServer(("0.0.0.0", 13000))

print("Listening on port 13000...")

server.register_function(subject_analysis, "subject_analysis")

server.serve_forever()