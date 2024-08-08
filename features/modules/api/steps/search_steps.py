import requests
from behave import *
from urllib.parse import quote, urljoin


@when('API: Call API for search for cat images')
def step_impl(context):

	endpoint    = 'v1/images/search'
	url = urljoin(context.base_url, endpoint)

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': context.api_key
    }

	params = {
        "size": "med",
        "mime_types": "jpg",
        "format": "json",
        "has_breeds": "true",
        "order": "RANDOM",
        "page": 0,
        "limit": 2
    }

	response = requests.get(url, headers=headers, params=params, verify=False)
	context.status_code = str(response.status_code)
	context.response_body = response.json()
	print(f'STATUS CODE = {context.status_code}')

	print(f'REPONSE STATUS CODE = {context.response_body}')
	assert True

@when('API: Call API for search for cat images with an invalid api-key')
def step_impl(context):

	endpoint    = 'v1/images/search'
	url = urljoin(context.base_url, endpoint)

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': context.api_key
    }

	params = {
        "size": "med",
        "mime_types": "jpg",
        "format": "json",
        "has_breeds": "true",
        "order": "RANDOM",
        "page": 0,
        "limit": 2
    }

	response = requests.get(url, headers=headers, params=params, verify=False)
	context.status_code = str(response.status_code)
	context.response_body = response.json()
	print(f'STATUS CODE = {context.status_code}')

	print(f'REPONSE STATUS CODE = {context.response_body}')
	assert True

@when('API: Call API for search for cat images with invalid limit')
def step_impl(context):
	
	endpoint    = 'v1/images/search'
	url = urljoin(context.base_url, endpoint)

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': context.api_key
    }

	params = {
        "limit": -10
    }

	response = requests.get(url, headers=headers, params=params, verify=False)
	context.status_code = str(response.status_code)
	context.response_body = response.json()
	print(f'STATUS CODE = {context.status_code}')

	print(f'REPONSE STATUS CODE = {context.response_body}')
	assert True



