import json, urlparse
from BaseHTTPServer import BaseHTTPRequestHandler
from search.twittersearch import TwitterSearch

class WebRankAPIHandler(BaseHTTPRequestHandler):
	"""
	Handles 2 kind of requests:
		- Normal webserver requests
		- Requests to the API, from the AJAX webrank engine.
	Author tom@0x101.com
	"""
	def __setHeaders(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

	def __getResponseContent(self, searchTerm, searchRank):
		response = {}
		response['searchTerm'] = searchTerm
		response['searchRank'] = searchRank
		return json.dumps(response)

	def __getSearchRank(self, searchTerm):
		twitterSearch = TwitterSearch()
		return twitterSearch.getSearchRank(searchTerm)
	
	def __getParamFromRequest(self, paramName):
		request = self.path.split('?', 1)
		paramValue = ''
		requestContent = ''
		if len(request) > 1:
			requestContent = request[1]
			params = urlparse.parse_qs(requestContent)
			try:
				paramValue = params[paramName].pop()
			except KeyError:
				paramValue = ''
		return paramValue

	def renderFile(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		f = open('../'+self.path, "r")
		self.wfile.write(f.read())

	def do_GET(self):
		searchTerm = self.__getParamFromRequest('searchTerm')
		if searchTerm != '':
			searchRank = self.__getSearchRank(searchTerm)
			self.__setHeaders()
			response = self.__getResponseContent(searchTerm, searchRank)
			self.wfile.write(response)
		else:
			# Webserver mode, render the requested file 
			self.renderFile()
