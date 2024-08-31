import time
from behave import *
from selenium.webdriver.common.keys import Keys

@when('UI - Product: The user add the product "{product}" to the cart')
def step_impl(context, product):
	context.products_page.hover_on_product_and_add_to_cart(product)


@then('UI - Product: The cart icon is updated and contains "{count_products}" products')
def step_impl(context, count_products):
	context.products_page.check_minicart_product_count(count_products)

@when('UI - Product: The user goes to cart')
def step_impl(context):
	time.sleep(2)
	context.products_page.open_minicart()
	context.products_page.minicart_pop_up.wait_until(method=lambda el: el.present, timeout=5)
	context.products_page.view_and_edit_cart_btn.click()



# @then('UI: The user open a product')
# def step_impl(context):
# 	context.products_page.product.click()

# @then('UI: The user add a product to cart')
# def step_impl(context):
# 	context.products_page.product.click()

# @then('UI: The product details is opened')
# def step_impl(context):
# 	context.base_page.verify_that_element_is_displayed(context.products_page.product_info)


	
# @when('UI: I search for course "{course}"')
# def step_impl(context, course):
# 	context.products_page.search_box.send_keys(course)
# 	context.products_page.search_box.send_keys(Keys.RETURN)
    
# @then('UI: The course "{course}" is visible')
# def step_impl(context, course):
# 	assert context.products_page.is_course_visible(course), f"The course '{course}' is not visible"