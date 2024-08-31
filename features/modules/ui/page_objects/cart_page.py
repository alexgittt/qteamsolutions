from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *

class CartPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context


    super().__init__(self.browser, self.context)

  def check_the_product_is_visible_on_cart(self, product):
      product_item = self.browser.element(xpath=f"//tr[contains(@class, 'item-info')]//strong[@class='product-item-name']/a[text()={product}]")
      product_item.wait_until(method=lambda e: e.present, timeout=5)
      
      assert product_item.present, f"Product '{product}' is not visible in the cart."