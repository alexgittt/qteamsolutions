import time
from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *
from features.modules.ui.buyer_address import buyers

class MainPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context


    self.navbar                       = self.browser.element(id="ui-id-2")
    self.bags_page                    = self.browser.element(xpath=f"//div[@class='categories-menu']//ul[@class='items']//a[text()='Bags']")
    self.gear_page                    = self.browser.element(class_name="base", text="Gear")
    # Shipping address fields
    self.shipping_address_page        = self.browser.div(class_name="step-title", text="Shipping Address")
    self.email                        = self.browser.element(id="customer-email-fieldset").element(id="customer-email")
    self.first_name                   = self.browser.element(name="firstname")
    self.last_name                    = self.browser.element(name="lastname")
    self.street                       = self.browser.element(name="street[0]")
    self.city                         = self.browser.element(name="city")
    self.state                        = self.browser.element(name="region_id")
    self.postal_code                  = self.browser.element(name="postcode")
    self.country                      = self.browser.element(name="country_id")
    self.phone_number                 = self.browser.element(name="telephone")
    self.shipping_method              = self.browser.element(id="checkout-shipping-method-load")
    self.continue_btn                 = self.browser.element(class_name="button action continue primary")
    # Payment screen
    self.payment_field                = self.browser.element(id="payment")
    self.place_order_btn              = self.browser.element(tag_name="button", text="Place Order")
    
    self.order_successful             = self.browser.element(class_name="base", text="Thank you for your purchase!")
    self.field_error_message          = self.browser.div(class_name="field-error", text="This is a required field.")


    super().__init__(self.browser, self.context)

  def fill_the_shipping_address(self, buyer):
      buyer_details = buyers.get(buyer)
      
      self.email.wait_until(method=lambda e: e.present and e.enabled, timeout=10).click()
      self.email.send_keys(buyer_details['email'])
      self.first_name.send_keys(buyer_details['first_name'])
      self.last_name.send_keys(buyer_details['last_name'])
      self.street.send_keys(buyer_details['street'])
      self.city.send_keys(buyer_details['city'])
      self.select_country(buyer_details['country'])
      self.select_state(buyer_details['state'])
      self.postal_code.send_keys(buyer_details['postal_code'])
      self.phone_number.send_keys(buyer_details['phone_number'])
      time.sleep(3)
      self.continue_btn.click()
  
  def select_state(self, state_name):
        try:
            self.state.click()
            self.state.wait_until(method=lambda e: e.present, timeout=10)

            options = self.state.elements(tag_name='option')

            for option in options:
                if option.text == state_name:
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", option)
                    option.click()
                    print(f"Country/Region '{state_name}' selected successfully.")
                    return
            
            print(f"Option '{state_name}' not found in the dropdown.")
            raise ValueError(f"Option '{state_name}' not found in the dropdown.")

        except Exception as e:
            print(f"An error occurred while selecting the country/region: {str(e)}")
            raise
        
  def select_country(self, country_name):
        try:
            self.state.click()
            options = self.country.elements(tag_name='option')

            for option in options:
                if option.text == country_name:
                    option.click()
                    print(f"Country/Region '{country_name}' selected successfully.")
                    return
            
            print(f"Option '{country_name}' not found in the dropdown.")
            raise ValueError(f"Option '{country_name}' not found in the dropdown.")

        except Exception as e:
            print(f"An error occurred while selecting the country/region: {str(e)}")
            raise
  
  def scroll_page(self):
      self.browser.execute_script("window.scrollBy(0, 300);")

  def place_order(self):
      self.place_order_btn.wait_until(method=lambda e: e.present and e.enabled, timeout=10)
      time.sleep(2)
      self.place_order_btn.click()

      



