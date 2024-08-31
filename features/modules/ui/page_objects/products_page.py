import time
from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *
from features.modules.ui.page_objects.base_page import *

class ProductsPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context

    self.product                   = self.browser.element(class_name="product-item-link")
    self.product_info              = self.browser.div(class_name="product-info-main")

    self.product_list              = self.browser.element(id="maincontent")
    self.add_to_cart_button        = self.product_list.button(class_name="action tocart primary")
    self.minicart_btn              = self.browser.div(class_name="minicart-wrapper")
    self.minicart_pop_up           = self.browser.div(class_name="minicart-wrapper active")
    self.view_and_edit_cart_btn    = self.browser.element(({'class':['action', 'viewcart']}))





    super().__init__(self.browser, self.context)


  def hover_on_product_and_add_to_cart(self, product):
      product = self.product_list.element(xpath=f"//a[@class='product-item-link' and normalize-space(text())='{product}']").wait_until(method=lambda e: e.present, timeout=5)
      product.hover()
    
      self.add_to_cart_button.wait_until(method=lambda e: e.present, timeout=5)
      self.add_to_cart_button.click()

  def check_minicart_product_count(self, expected_count):
      try:
          minicart_counter = self.browser.element(xpath="//div[@data-block='minicart']//span[@class='counter-number']")
          minicart_counter.wait_until(method=lambda e: e.present and e.text.strip() != "", timeout=10)
          actual_count = minicart_counter.text.strip()
          expected_count = str(expected_count)

          assert actual_count == expected_count, f"Expected {expected_count} items in the minicart, but found {actual_count}."

          return actual_count == expected_count

      except Exception as e:
          print(f"An error occurred: {str(e)}")
          raise
    
  def open_minicart(self):
      self.minicart_btn.click()

  