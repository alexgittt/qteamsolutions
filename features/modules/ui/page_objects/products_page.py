from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *

class ProductsPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context

    self.products_title        = self.browser.element(class_name="collections__heading", text="Products")
    self.products_list_parent  = self.browser.element(class_name="collections__product-cards")
    self.products_list         = self.products_list_parent.element(class_name="products__list")


    super().__init__(self.browser, self.context)
