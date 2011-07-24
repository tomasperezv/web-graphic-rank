#!/usr/bin/python2.6
from core.server import WebRankAPIServer

def main():
	"""
	A simple webserver/API which return the rank for search terms. Used by a js frontend to render a
	graph.
	Author tom@0x101.com
	"""
	try:
		print 'starting webserver\n'
		webRankAPIServer = WebRankAPIServer(8080)
		webRankAPIServer.start()

	except KeyboardInterrupt:
		print 'stopping webserver\n'
		webRankAPIServer.stop()

if __name__ == '__main__':
	main()

