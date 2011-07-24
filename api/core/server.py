from BaseHTTPServer import HTTPServer
from handler import WebRankAPIHandler 

class WebRankAPIServer():
	"""
	Basic wrapper for the HTTPServer object
	Author tom@0x101.com
	"""
	__port = 8080
	__server = None

	def __init__(self, port):
		self.__port = port

	def start(self):
		self.__server = HTTPServer(('', self.__port), WebRankAPIHandler)
		self.__server.serve_forever()

	def stop(self):
		self.__server.socket.close()
