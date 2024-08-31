import time
from behave import *
from features.modules.ui.credentials import users



@given('UI - Main: The user is on the home page')
def step_impl(context):
	context.main_page.go_to_url(context.url)
	context.base_page.verify_that_element_is_displayed(context.main_page.navbar)

@when('UI - Main: The user goes to the category {category} products page')
def step_impl(context, category):
	context.base_page.go_to_main_category(category)

@when('UI - Main: The user goes to the sub-category {sub_category} products page')
def step_impl(context, sub_category):
	context.base_page.go_to_sub_category(sub_category)
	
@then('UI - Main: The page {page} is opened')
def step_impl(context, page):
	context.base_page.verify_that_page_product_is_displayed(page)

