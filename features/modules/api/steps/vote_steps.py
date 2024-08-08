import json
import requests
from behave import *
from urllib.parse import quote, urljoin


@when('API: Call API to vote a cat image')
def step_impl(context):
	
	endpoint    = 'v1/votes'
	url = urljoin(context.base_url, endpoint)

	payload = {
		"image_id":"asf2",
		"sub_id": "my-user-1234",
		"value":1
		}

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': context.api_key
    }
	

	response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
	context.status_code = str(response.status_code)
	context.response_body = response.json()

	print(f'STATUS CODE = {context.status_code}')

	print(f'REPONSE STATUS CODE = {context.response_body}')
	assert True

@then('API: The status code is "{status_code}"')
def step_impl(context, status_code):
	assert context.status_code == status_code, f"Expected status code to be {status_code} but it is {context.status_code} | Response: {context.response_body}"

@then('API: Check the response data is correct')
def step_impl(context):
	data = context.response_body

	assert len(data) > 0, "Response list should not be empty"

	cat_data = data[0]
	assert "breeds" in cat_data, "'breeds' key is missing in the response"
	assert len(cat_data["breeds"]) > 0, "'breeds' list should not be empty"

	breed_info = cat_data["breeds"][0]
	assert "name" in breed_info, "'name' key is missing in the breed info"
	assert "description" in breed_info, "'description' key is missing in the breed info"
	assert "temperament" in breed_info, "'temperament' key is missing in the breed info"

	print("Cat Breed Name:", breed_info["name"])
	print("Description:", breed_info["description"])
	print("Temperament:", breed_info["temperament"])


@then('API: Check the message is "{expected_status}"')
def step_impl(context, expected_status):
	data = context.response_body

	current_status = data["message"]

	assert expected_status in current_status, "'SUCCESS' key is missing in the response"

@then('API: Check the error message is "{expected_message}"')
def step_impl(context, expected_message):

	assert expected_message in context.error_message, f"The error message in response does not match, the current one is: {context.error_message}"

@when('API: Call API to vote a cat image with an invalid x-api-key')
def step_impl(context):
	
	endpoint    = 'v1/votes'
	url = urljoin(context.base_url, endpoint)

	payload = {
		"image_id":"asf2",
		"sub_id": "my-user-1234",
		"value":1
		}

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': 'invalid'
    }
	

	response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
	context.status_code = str(response.status_code)
	context.error_message = response.text

@when('API: Call API to vote a cat image with no image id')
def step_impl(context):

	endpoint    = 'v1/votes'
	url = urljoin(context.base_url, endpoint)

	payload = {
		"image_id":"",
		"sub_id": "my-user-1234",
		"value":1
		}

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': context.api_key
    }
	

	response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
	context.status_code = str(response.status_code)
	# context.response_body = response.json()
	context.error_message = response.text
