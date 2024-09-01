import time
from behave import *
from selenium.webdriver.common.keys import Keys


@then('UI - Cart: The cart icon is updated and contains "{count_products}" products')
def step_impl(context, count_products):
	context.products_page.check_minicart_product_count(count_products)

@when('UI - Cart: The user goes to cart')
def step_impl(context):
	context.products_page.open_minicart()
	context.products_page.minicart_pop_up.wait_until(method=lambda el: el.present, timeout=5)
	context.products_page.view_and_edit_cart_btn.click()

@when('UI - Cart: The user goes to the empty cart')
def step_impl(context):
	context.products_page.open_minicart()

@then('UI - Cart: Check the product {product} is visible on the cart')
def step_impl(context, product):
	context.cart_page.check_the_product_is_visible_on_cart(product)

@then('UI - Cart: Empty message is displayed')
def step_impl(context):
	context.cart_page.empty_cart_message.wait_until(method=lambda el: el.present, timeout=5)

@when('UI - Cart: The user delete the product from the cart')
def step_impl(context):
	context.cart_page.delete_product.click()

@then('UI - Cart: The shopping cart main page is empty')
def step_impl(context):
	context.cart_page.empty_shopping_cart_page.wait_until(method=lambda el: el.present, timeout=5)

@when('UI - Cart: The user update the quantity of the product to {quantity}')
def step_impl(context, quantity):
	context.cart_page.clear_quantity_field()
	context.cart_page.quantity.send_keys(quantity)
	context.cart_page.update_cart_btn.click()

@then('UI - Cart: The quantity is {quantity}')
def step_impl(context, quantity):
	context.cart_page.check_quantity_value(quantity)