import json
import requests
from behave import *
from urllib.parse import quote, urljoin

@then('API: The status code is "{status_code}"')
def step_impl(context, status_code):
	assert context.status_code == status_code, f"Expected status code to be {status_code} but it is {context.status_code} | Response: {context.response_body}"

@then('API: Check the message is "{expected_status}"')
def step_impl(context, expected_status):
	data = context.response_body

	current_status = data["message"]

	assert expected_status in current_status, "'SUCCESS' key is missing in the response"

@then('API: Check the error message is "{expected_message}"')
def step_impl(context, expected_message):

	assert expected_message in context.error_message, f"The error message in response does not match, the current one is: {context.error_message}"
	
