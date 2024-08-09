from behave import *

@then('UI: I can see the products page')
def step_impl(context):
	context.base_page.verify_that_element_is_displayed(context.products_page.products_title)
	context.base_page.verify_that_element_is_displayed(context.products_page.products_list)
	