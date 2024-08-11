import time
from behave import *
from selenium.webdriver.common.keys import Keys

@then('UI: I can see the products page')
def step_impl(context):
	context.base_page.verify_that_element_is_displayed(context.products_page.products_title)
	context.base_page.verify_that_element_is_displayed(context.products_page.products_list)
	
@when('UI: I search for course "{course}"')
def step_impl(context, course):
	context.products_page.search_box.send_keys(course)
	context.products_page.search_box.send_keys(Keys.RETURN)
    
@then('UI: The course "{course}" is visible')
def step_impl(context, course):
	assert context.products_page.is_course_visible(course), f"The course '{course}' is not visible"