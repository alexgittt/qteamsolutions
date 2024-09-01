from behave import *

from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.cart_page import *
from features.modules.ui.page_objects.main_page import *
from features.modules.ui.page_objects.products_page import *


@given('UI: Initialize Pages')
def step_impl(context):

	# ALL page objects initialization
	context.base_page 		= BasePage(context.browser, context)
	context.main_page 		= MainPage(context.browser, context)
	context.cart_page 		= CartPage(context.browser, context)
	context.products_page	= ProductsPage(context.browser, context)