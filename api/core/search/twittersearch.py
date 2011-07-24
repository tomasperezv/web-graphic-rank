import json, httplib, urllib, sys, os
from search import Search

class TwitterSearch(Search):
	"""
	Author tom@0x101.com
	@see https://dev.twitter.com/docs/api/1/get/search
	"""
	__host = 'search.twitter.com'
	__searchTerm = None

	def __getParams(self, searchTerm):
		return urllib.urlencode([
				('q', searchTerm),
				('result_type', 'mixed'),
			])
	
	def __getConnection(self, params):
		connection = httplib.HTTPConnection(self.__host)
		connection.request('GET', '/search.json?'+params)
		return connection

	def __getResponse(self, params):
		connection = self.__getConnection(params)
		response = connection.getresponse()
		rawResponse = response.read()
		connection.close
		return rawResponse 

	def getSearchRank(self, searchTerm):
		"""
		We are just calculating the popularity of the search term, based on the
		number of results that we receive.
		"""
		params = self.__getParams(searchTerm)
		rawResponse = self.__getResponse(params)
		response = json.loads(rawResponse)
		return len(response['results'])
