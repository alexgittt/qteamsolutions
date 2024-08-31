import time
from behave import *
from selenium.webdriver.common.keys import Keys


@then('UI - Cart: The cart icon is updated and contains "{count_products}" products')
def step_impl(context, count_products):
	context.products_page.check_minicart_product_count(count_products)

@when('UI - Cart: The user goes to cart')
def step_impl(context):
	time.sleep(2)
	context.products_page.open_minicart()
	context.products_page.minicart_pop_up.wait_until(method=lambda el: el.present, timeout=5)
	context.products_page.view_and_edit_cart_btn.click()

@then('UI - Cart: Check the product {product} is visible on the cart')
def step_impl(context, product):
	context.cart_page.check_the_product_is_visible_on_cart(product)