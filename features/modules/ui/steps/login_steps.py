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

@then('UI: Error message is diplayed')
def step_impl(context):
    context.base_page.verify_that_element_is_displayed(context.login_page.login_error)
	
@when('UI: I login with user "{user}"')
def step_impl(context, user):
	user_details = users.get(user)
	context.login_page.email.send_keys(user_details['username'])
	context.login_page.password.send_keys(user_details['password'])
	context.login_page.signin_btn.click()
	
@when('UI: I log out')
def step_impl(context):
	context.login_page.account_dropdown.click()
	context.login_page.sign_out_btn.click()
	context.login_page.sign_in_btn.click()
	
@then('UI: I am logged in')
def step_impl(context):
	context.base_page.verify_that_element_is_displayed(context.login_page.my_dashboard)
	
@then('UI: I am logged out')
def step_impl(context):
	context.base_page.verify_that_element_is_displayed(context.login_page.sign_in_btn)