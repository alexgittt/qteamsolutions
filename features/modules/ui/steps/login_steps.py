import time
from behave import *
from features.modules.ui.credentials import users



@given('UI: I go to automation page')
def step_impl(context):
	context.login_page.go_to_url(context.url)
	context.base_page.verify_that_element_is_displayed(context.login_page.automation_page)

@when('UI: I go to "{link_name}" page')
def step_impl(context, link_name):
	context.base_page.click_on_link(link_name)
	
@then('UI: I check that Login Automation page is opened')
def step_impl(context):
    context.base_page.verify_that_element_is_displayed(context.login_page.login_screen)
	
# @when('UI: I create a new account with "{user_account}"')
# def step_impl(context, user_account):
# 	account_details = accounts.get(user_account)
# 	if account_details is None:
# 		print(f"Available accounts: {list(accounts.keys())}")  # Debug print
# 		raise ValueError(f"No account details found for: {user_account}")
	
# 	context.login_page.first_name.send_keys(account_details['first_name'])
# 	context.login_page.last_name.set(account_details['last_name'])
# 	context.login_page.email.set(account_details['email'])
# 	context.login_page.password.set(account_details['password'])
# 	context.login_page.checkbox_terms.click()
# 	context.login_page.sign_up.click()
# 	time.sleep(5)

	
@when('UI: I login with user "{user}"')
def step_impl(context, user):
	user_details = users.get(user)
	context.login_page.email.send_keys(user_details['username'])
	context.login_page.password.send_keys(user_details['password'])
	context.login_page.signin_btn.click()
	time.sleep(15)
	
@then('UI: I am logged in')
def step_impl(context):
	context.base_page.verify_that_element_is_displayed(context.login_page.my_dashboard)