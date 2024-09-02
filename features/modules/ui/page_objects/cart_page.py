from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *
from selenium.webdriver.common.keys import Keys

class CartPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context

    self.empty_cart_message           = self.browser.element(class_name="subtitle empty", text="You have no items in your shopping cart.")
    self.delete_product               = self.browser.element(class_name="action-delete")
    self.empty_shopping_cart_page     = self.browser.div(class_name="cart-empty")
    self.quantity                     = self.browser.element(class_name="input-text qty")
    self.update_cart_btn              = self.browser.element(tag_name="button", class_name="action update")
    self.checkout_btn                 = self.browser.element(data_role="proceed-to-checkout")
    


    super().__init__(self.browser, self.context)

  def check_the_product_is_visible_on_cart(self, product):
      product_item = self.browser.element(xpath=f"//tr[contains(@class, 'item-info')]//strong[@class='product-item-name']/a[text()={product}]")
      product_item.wait_until(method=lambda e: e.present, timeout=5)
      
      assert product_item.present, f"Product '{product}' is not visible in the cart."

  def check_quantity_value(self, expected_quantity):
      current_value = self.quantity.get_attribute('value')

      print(f"Current Value: '{current_value}' (type: {type(current_value)})")
      print(f"Expected Quantity: '{expected_quantity}' (type: {type(expected_quantity)})")

      expected_quantity = expected_quantity.strip('"')
      
      assert str(current_value) == str(expected_quantity), f"Expected quantity {expected_quantity}, but found {current_value}"

  def clear_quantity_field(self):
      self.quantity.click()
      self.quantity.send_keys(Keys.COMMAND + 'a')
      self.quantity.send_keys(Keys.BACKSPACE)