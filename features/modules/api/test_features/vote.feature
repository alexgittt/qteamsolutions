Feature: THE-CAT-API-VOTE
    
    @api
	Scenario: Vote a cat image
	When API: Call API to vote a cat image
    Then API: The status code is "201"
    Then API: Check the message is "SUCCESS"

    @api
	Scenario: Vote a cat image with no image id
	When API: Call API to vote a cat image with no image id
    Then API: The status code is "400"
    Then API: Check the error message is ""image_id" is not allowed to be empty"

    @api
	Scenario: Vote a cat image with an invalid x-api-key
	When API: Call API to vote a cat image with an invalid x-api-key
    Then API: The status code is "401"
    Then API: Check the error message is "AUTHENTICATION_ERROR"
