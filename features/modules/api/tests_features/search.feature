Feature: THE-CAT-API-SEARCH

	@api
	Scenario: Search for cat images
	When API: Call API for search for cat images
    Then API: The status code is "200"
    Then API: Check the response data is correct

    @api
	Scenario: Search for cat images with an invalid api-key
	When API: Call API for search for cat images with an invalid api-key
    Then API: The status code is "200"
    Then API: Check the response data is correct

    @api
	Scenario: Search for cat images with invalid limit
	When API: Call API for search for cat images with invalid limit
    Then API: The status code is "400"
