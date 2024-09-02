import time
from behave import *




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

@then('UI - Main: The shipping address page is displayed')
def step_impl(context):
	context.main_page.shipping_address_page.wait_until(method=lambda e: e.present, timeout=10)

@when('UI - Main: The user fill the shipping address with the address "{buyer}"')
def step_impl(context, buyer):
	context.main_page.fill_the_shipping_address(buyer)

@then('UI - Main: The payment screen is displayed')
def step_impl(context):
	context.main_page.payment_field.wait_until(method=lambda e: e.present, timeout=10)

@when('UI - Main: The user place order')
def step_impl(context):
	context.main_page.place_order()

@then('UI - Main: The order is successfully placed')
def step_impl(context):
	context.main_page.order_successful.wait_until(method=lambda e: e.present, timeout=10)