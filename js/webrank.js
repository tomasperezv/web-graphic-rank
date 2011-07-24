/**
 * Static objec which manages connections to the webrank API.
 */
var WebRank = {

	/**
	 * Time used by the update interval to request the
	 * rank values from the API
	 * @var refreshTime
	 */
	refreshTime: 10000,


	/**
	 * Performs a request agains the webrank API, returns the
	 * searchRank value to the optional callback.
	 * @param {String} searchTerm
	 * @param {Function} callback
	 */
	getWebRank: function(searchTerm, callback) {
		new Ajax.Request('/api/?searchTerm='+searchTerm,
		{
			method:'get',
			onSuccess: function(transport){

				var response = transport.responseText || "no response text";

				if (typeof callback !== 'undefined') {
					callback(transport.responseJSON.searchRank);
				}

			}
		});
	}
};
