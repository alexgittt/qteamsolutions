from behave import *

from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.login_page import *
from features.modules.ui.page_objects.products_page import *


@given('UI: Initialize Pages')
def step_impl(context):

	# ALL page objects initialization
	context.base_page 		= BasePage(context.driver, context)
	context.login_page 		= LoginPage(context.driver, context)
	context.products_page	= ProductsPage(context.driver, context)