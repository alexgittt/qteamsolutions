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

	print(f'REPONSE BODY = {context.response_body}')
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

	print(f'REPONSE BODY = {context.response_body}')

@when('API: Call API for search for cat images with "{invalid_limit}"')
def step_impl(context, invalid_limit):
	
	endpoint    = 'v1/images/search'
	url = urljoin(context.base_url, endpoint)

	headers = {
            'Content-Type': 'application/json',
			'x-api-key': context.api_key
    }

	params = {
        "limit": invalid_limit
    }

	response = requests.get(url, headers=headers, params=params, verify=False)
	context.status_code = str(response.status_code)
	context.response_body = response.json()
	print(f'STATUS CODE = {context.status_code}')

	print(f'REPONSE BODY = {context.response_body}')
	assert True

@then('API: Check the response data is correct')
def step_impl(context):
    
	data = context.response_body

	assert len(data) > 0, "Response list should not be empty"

	for cat_data in data:
		assert "breeds" in cat_data, "'breeds' key is missing in the response"
		assert len(cat_data["breeds"]) > 0, "'breeds' list should not be empty"

		breed_info = cat_data["breeds"][0]
		assert "name" in breed_info, "'name' key is missing in the breed info"
		assert "description" in breed_info, "'description' key is missing in the breed info"
		assert "temperament" in breed_info, "'temperament' key is missing in the breed info"

		print("Cat Breed Name:", breed_info["name"])
		print("Description:", breed_info["description"])
		print("Temperament:", breed_info["temperament"])


