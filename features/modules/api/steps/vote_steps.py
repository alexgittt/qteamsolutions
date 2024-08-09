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

	print(f'REPONSE BODY = {context.response_body}')
	assert True



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
