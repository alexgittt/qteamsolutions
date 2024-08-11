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
	Scenario Outline: Search for cat images with invalid limit items "<invalid_limit>"
	    When API: Call API for search for cat images with limit items "<invalid_limit>"
        Then API: The status code is "400"

        Examples:
    	| invalid_limit |
    	| -10           |
    	| abc           |
    	| @#$$$$        |

		
